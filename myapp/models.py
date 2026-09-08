from django.db import models


class PredictionHistory(models.Model):
    symptoms = models.TextField(help_text="Comma-separated symptom keys that were selected")
    predicted_disease = models.CharField(max_length=200)
    top_matches = models.TextField(blank=True, help_text="JSON string of top-3 disease/confidence pairs")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.predicted_disease} ({self.created_at:%Y-%m-%d %H:%M})"

    def symptom_list(self):
        return [s for s in self.symptoms.split(",") if s]
