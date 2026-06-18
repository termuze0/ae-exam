from django.db import models
from django.contrib.auth.hashers import make_password
from cloudinary.models import CloudinaryField
from django.contrib.auth import get_user_model

User = get_user_model()

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




class ExamSession(models.Model):
    """Tracks a student's active exam attempt."""
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name="exam_sessions")
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name="sessions")
    started_at = models.DateTimeField(auto_now_add=True)
    submitted = models.BooleanField(default=False)

    class Meta:
        # One active session per student per exam
        unique_together = ("student", "exam")

    def __str__(self):
        return f"{self.student} – {self.exam} ({'done' if self.submitted else 'active'})"


class StudentAnswer(models.Model):
    """One selected answer per question per session."""
    session = models.ForeignKey(ExamSession, on_delete=models.CASCADE, related_name="student_answers")
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_answer = models.ForeignKey(
        Answer,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    class Meta:
        unique_together = ("session", "question")

    @property
    def is_correct(self):
        return self.selected_answer is not None and self.selected_answer.is_correct

    def __str__(self):
        return f"Q{self.question_id} → {'✓' if self.is_correct else '✗'}"


class ExamResult(models.Model):
    """Computed score stored after submission."""
    session = models.OneToOneField(ExamSession, on_delete=models.CASCADE, related_name="result")
    score = models.PositiveIntegerField()          # correct answers count
    total = models.PositiveIntegerField()          # total questions
    passed = models.BooleanField(default=False)
    finished_at = models.DateTimeField(auto_now_add=True)

    PASS_THRESHOLD = 0.6  # 60 % to pass — adjust as needed

    def __str__(self):
        return f"{self.session.student} – {self.score}/{self.total}"