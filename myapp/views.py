from django.shortcuts import render
import os
import json
import joblib
import pandas as pd
from django.shortcuts import render, redirect

from .models import PredictionHistory

path = os.path.dirname(os.path.abspath(__file__))
model = joblib.load(os.path.join(path, "model.pkl"))
label_encoder = joblib.load(os.path.join(path, "label_encoder.pkl"))
symptom_columns = joblib.load(os.path.join(path, "symptom_columns.pkl"))


def _clean_label(s):
    return " ".join(s.replace("_", " ").split()).title()
def clear_history(req):
    if req.method == "POST":
        PredictionHistory.objects.all().delete()

    return redirect("history")


SYMPTOM_LABELS = [{"name": s, "label": _clean_label(s)} for s in symptom_columns]


def index(req):
    return render(req, "index.html")


def prediction(req):
    if req.method == 'POST':
        selected = set(req.POST.getlist('symptoms'))
        user_input = [1 if s in selected else 0 for s in symptom_columns]
        input_df = pd.DataFrame([user_input], columns=symptom_columns)
        result = model.predict(input_df)[0]
        res = label_encoder.inverse_transform([result])[0]

        top_matches = None
        if hasattr(model, "predict_proba"):
            proba = model.predict_proba(input_df)[0]
            top_idx = proba.argsort()[::-1][:3]
            top_matches = [
                {"disease": label_encoder.inverse_transform([i])[0],
                 "confidence": round(proba[i] * 100, 1)}
                for i in top_idx
            ]

        try:
            PredictionHistory.objects.create(
                symptoms=",".join(sorted(selected)),
                predicted_disease=res,
                top_matches=json.dumps(top_matches or []),
            )
        except Exception:
            # Don't let a DB/history failure break the prediction result itself
            # (e.g. no writable DB configured yet in this environment).
            pass

        return render(req, "prediction.html", {
            "res": res,
            "top_matches": top_matches,
            "symptoms": SYMPTOM_LABELS,
            "selected": selected,
        })
    return render(req, "prediction.html", {"symptoms": SYMPTOM_LABELS, "selected": set()})


def history(req):
    history_rows = []
    try:
        records = PredictionHistory.objects.all()
        for r in records:
            history_rows.append({
                "id": r.id,
                "created_at": r.created_at,
                "predicted_disease": r.predicted_disease,
                "symptoms": [_clean_label(s) for s in r.symptom_list()],
            })
    except Exception:
        pass
    return render(req, "history.html", {"history": history_rows})
