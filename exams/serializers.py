from rest_framework import serializers
from .models import Exam, Answer, Question, Passage, CustomUser
from djoser.serializers import UserCreateSerializer


# ── Passage ───────────────────────────────────────────────────────────────────

class PassageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passage
        fields = ['id', 'title', 'content', 'image']


# ── Answer ────────────────────────────────────────────────────────────────────

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['id', 'text', 'is_correct']


class AnswerWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['text', 'is_correct']


# ── Question ──────────────────────────────────────────────────────────────────

class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ['id', 'exam', 'passage', 'text', 'answers']


class QuestionWriteSerializer(serializers.ModelSerializer):
    answers = AnswerWriteSerializer(many=True)
    passage = PassageSerializer(required=False, allow_null=True)

    class Meta:
        model = Question
        fields = ['text', 'passage', 'answers']


# ── Exam ──────────────────────────────────────────────────────────────────────

class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = ['id', 'title', 'description', 'duration_minutes', 'is_active']


class ExamDetailSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Exam
        fields = ['id', 'title', 'description', 'duration_minutes', 'is_active', 'questions']


class ExamBulkUploadSerializer(serializers.ModelSerializer):
    questions = QuestionWriteSerializer(many=True)

    class Meta:
        model = Exam
        fields = ['title', 'description', 'duration_minutes', 'is_active', 'questions']

    def create(self, validated_data):
        questions_data = validated_data.pop('questions')
        exam = Exam.objects.create(**validated_data)

        for q_data in questions_data:
            answers_data = q_data.pop('answers')
            passage_data = q_data.pop('passage', None)

            passage = None
            if passage_data:
                passage = Passage.objects.create(**passage_data)

            question = Question.objects.create(exam=exam, passage=passage, **q_data)

            for a_data in answers_data:
                Answer.objects.create(question=question, **a_data)

        return exam


# ── User (Djoser) ────────────────────────────────────────────────────────────

class CustomUserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = CustomUser
        fields = ('id', 'username', 'password')