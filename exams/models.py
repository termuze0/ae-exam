from django.db import models
from django.contrib.auth.hashers import make_password
from cloudinary.models import CloudinaryField


class Exam(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    duration_minutes = models.PositiveIntegerField(default=60)
    is_active = models.BooleanField(default=True)
    password = models.CharField(max_length=255, blank=True, null=True)

    def set_password(self, raw_password):
        """Hash and store the password."""
        self.password = make_password(raw_password)

    def __str__(self):
        return self.title


class Passage(models.Model):
    title = models.CharField(max_length=255, blank=True)
    content = models.TextField()
    image = CloudinaryField(
        "image",
        folder="passage",
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.title or f"Passage {self.pk}"


class Question(models.Model):
    exam = models.ForeignKey(
        Exam,
        on_delete=models.CASCADE,
        related_name="questions",
    )
    passage = models.ForeignKey(
        Passage,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="questions",
    )
    text = models.TextField()

    def __str__(self):
        return self.text[:50]


class Answer(models.Model):
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name="answers",
    )
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text