from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import Exam, Answer, Question, Passage


# ── Passage ───────────────────────────────────────────────────────────────────

class PassageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passage
        fields = ["id", "title", "content", "image"]


class PassageWriteSerializer(serializers.ModelSerializer):
    """Used when creating a passage inline during bulk upload."""
    class Meta:
        model = Passage
        fields = ["title", "content", "image"]


# ── Answer ────────────────────────────────────────────────────────────────────

class AnswerSerializer(serializers.ModelSerializer):
    """Full answer — used by admin/staff views (includes is_correct)."""
    class Meta:
        model = Answer
        fields = ["id", "text", "is_correct"]


class AnswerStudentSerializer(serializers.ModelSerializer):
    """Student-safe answer — hides is_correct."""
    class Meta:
        model = Answer
        fields = ["id", "text"]


class AnswerWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ["text", "is_correct"]


# ── Question ──────────────────────────────────────────────────────────────────

class QuestionSerializer(serializers.ModelSerializer):
    """Full question with answers — for admin/staff use."""
    answers = AnswerSerializer(many=True, read_only=True)
    passage = PassageSerializer(read_only=True)

    class Meta:
        model = Question
        fields = ["id", "exam", "passage", "text", "answers"]


class QuestionStudentSerializer(serializers.ModelSerializer):
    """Student-safe question — answers omit is_correct."""
    answers = AnswerStudentSerializer(many=True, read_only=True)
    passage = PassageSerializer(read_only=True)

    class Meta:
        model = Question
        fields = ["id", "passage", "text", "answers"]


class QuestionWriteSerializer(serializers.ModelSerializer):
    """Used for nested write operations (bulk upload)."""
    answers = AnswerWriteSerializer(many=True)
    # Accept an optional inline passage object or a passage_id FK
    passage = PassageWriteSerializer(required=False, allow_null=True)

    class Meta:
        model = Question
        fields = ["text", "passage", "answers"]


# ── Exam ──────────────────────────────────────────────────────────────────────

class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = ["id", "title", "description", "duration_minutes", "is_active", "password"]
        extra_kwargs = {
            "password": {"write_only": True, "required": False, "allow_null": True},
        }

    def create(self, validated_data):
        raw_password = validated_data.pop("password", None)
        exam = Exam(**validated_data)
        if raw_password:
            exam.set_password(raw_password)
        exam.save()
        return exam

    def update(self, instance, validated_data):
        raw_password = validated_data.pop("password", None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if raw_password:
            instance.set_password(raw_password)
        instance.save()
        return instance


class ExamDetailSerializer(serializers.ModelSerializer):
    """
    Admin/staff detail view — includes correct answers.
    NOT returned to students.
    """
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Exam
        fields = ["id", "title", "description", "duration_minutes", "is_active", "questions"]


class ExamStudentSerializer(serializers.ModelSerializer):
    """
    Student-facing exam detail — answers never reveal is_correct.
    Returned after a successful password check.
    """
    questions = QuestionStudentSerializer(many=True, read_only=True)

    class Meta:
        model = Exam
        fields = ["id", "title", "description", "duration_minutes", "questions"]


class ExamPasswordCheckSerializer(serializers.Serializer):
    password = serializers.CharField(write_only=True)


class ExamBulkUploadSerializer(serializers.ModelSerializer):
    questions = QuestionWriteSerializer(many=True)

    class Meta:
        model = Exam
        fields = ["title", "description", "duration_minutes", "is_active", "password", "questions"]
        extra_kwargs = {
            "password": {"write_only": True, "required": False, "allow_null": True},
        }

    def create(self, validated_data):
        questions_data = validated_data.pop("questions")
        raw_password = validated_data.pop("password", None)

        exam = Exam(**validated_data)
        if raw_password:
            exam.set_password(raw_password)
        exam.save()

        for q_data in questions_data:
            answers_data = q_data.pop("answers")
            passage_data = q_data.pop("passage", None)

            passage = None
            if passage_data:
                # Avoid duplicates: match on title + content
                passage, _ = Passage.objects.get_or_create(
                    title=passage_data.get("title", ""),
                    content=passage_data["content"],
                    defaults=passage_data,
                )

            question = Question.objects.create(exam=exam, passage=passage, **q_data)

            for a_data in answers_data:
                Answer.objects.create(question=question, **a_data)

        return exam