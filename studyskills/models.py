from django.db import models

from django.contrib.auth.models import User

class StudySkillsResult(models.Model):
    """
        Stores students reponses to study skills assessment.
    """
    student = models.ForeignKey(User)
    answers = models.TextField()
    date_taken = models.DateTimeField(auto_now_add=True)
