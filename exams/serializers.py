from rest_framework import serializers
from .models import Exam, Question, Answer


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = [
            'id',
            'text',
            'is_correct'
        ]


class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = Question
        fields = [
            'id',
            'text',
            'answers'
        ]


class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = [
            'id',
            'title',
            'description',
            'duration_minutes'
        ]


class ExamDetailSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = Exam
        fields = [
            'id',
            'title',
            'description',
            'duration_minutes',
            'questions'
        ]