from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from django.shortcuts import get_object_or_404
from django.db import transaction
from django.contrib.auth.hashers import check_password

from .models import Exam, Passage, Question, Answer
from .serializers import (
    ExamSerializer,
    ExamDetailSerializer,
    ExamStudentSerializer,
    ExamBulkUploadSerializer,
    ExamPasswordCheckSerializer,
    PassageSerializer,
    QuestionSerializer,
    AnswerSerializer,
)


# ── Exam ──────────────────────────────────────────────────────────────────────

class ExamListAPIView(APIView):
    def get(self, request):
        exams = Exam.objects.all().order_by("-id")
        return Response(ExamSerializer(exams, many=True).data)

    def post(self, request):
        serializer = ExamSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ExamDetailAPIView(APIView):
    def get_object(self, pk):
        return get_object_or_404(Exam, pk=pk)

    def get(self, request, pk):
        # Admin/staff view — full detail with correct answers
        return Response(ExamDetailSerializer(self.get_object(pk)).data)

    def put(self, request, pk):
        serializer = ExamSerializer(self.get_object(pk), data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def patch(self, request, pk):
        serializer = ExamSerializer(self.get_object(pk), data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        self.get_object(pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ExamBulkUploadAPIView(APIView):
    def post(self, request):
        serializer = ExamBulkUploadSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        with transaction.atomic():
            exam = serializer.save()
        return Response(ExamDetailSerializer(exam).data, status=status.HTTP_201_CREATED)


class ExamStartAPIView(APIView):
    """
    Student submits the exam password here.

    - If the exam has no password, return the student-safe exam data directly.
    - If it has a password and the submitted one matches, return student-safe data.
    - If the password is wrong, return 403.
    - Correct answers (is_correct) are NEVER included in the response.
    """
    def post(self, request, pk):
        exam = get_object_or_404(Exam, pk=pk)
        serializer = ExamPasswordCheckSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        submitted_password = serializer.validated_data["password"]

        if exam.password:
            if not check_password(submitted_password, exam.password):
                return Response(
                    {"detail": "Incorrect exam password."},
                    status=status.HTTP_403_FORBIDDEN,
                )

        # Return student-safe serializer (no is_correct leak)
        return Response(ExamStudentSerializer(exam).data, status=status.HTTP_200_OK)


# ── Passage ───────────────────────────────────────────────────────────────────

class PassageListAPIView(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def get(self, request):
        passages = Passage.objects.all().order_by("-id")
        return Response(PassageSerializer(passages, many=True).data)

    def post(self, request):
        serializer = PassageSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class PassageDetailAPIView(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def get_object(self, pk):
        return get_object_or_404(Passage, pk=pk)

    def get(self, request, pk):
        return Response(PassageSerializer(self.get_object(pk)).data)

    def put(self, request, pk):
        serializer = PassageSerializer(self.get_object(pk), data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def patch(self, request, pk):
        serializer = PassageSerializer(self.get_object(pk), data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        self.get_object(pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ── Question ──────────────────────────────────────────────────────────────────

class QuestionListAPIView(APIView):
    def get(self, request):
        exam_id = request.query_params.get("exam")
        qs = Question.objects.select_related("passage").prefetch_related("answers").order_by("-id")
        if exam_id:
            qs = qs.filter(exam_id=exam_id)
        return Response(QuestionSerializer(qs, many=True).data)

    def post(self, request):
        serializer = QuestionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class QuestionDetailAPIView(APIView):
    def get_object(self, pk):
        return get_object_or_404(
            Question.objects.select_related("passage").prefetch_related("answers"), pk=pk
        )

    def get(self, request, pk):
        return Response(QuestionSerializer(self.get_object(pk)).data)

    def put(self, request, pk):
        serializer = QuestionSerializer(self.get_object(pk), data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def patch(self, request, pk):
        serializer = QuestionSerializer(self.get_object(pk), data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        self.get_object(pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ── Answer ────────────────────────────────────────────────────────────────────

class AnswerListAPIView(APIView):
    def get(self, request):
        question_id = request.query_params.get("question")
        qs = Answer.objects.all().order_by("-id")
        if question_id:
            qs = qs.filter(question_id=question_id)
        return Response(AnswerSerializer(qs, many=True).data)

    def post(self, request):
        serializer = AnswerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class AnswerDetailAPIView(APIView):
    def get_object(self, pk):
        return get_object_or_404(Answer, pk=pk)

    def get(self, request, pk):
        return Response(AnswerSerializer(self.get_object(pk)).data)

    def put(self, request, pk):
        serializer = AnswerSerializer(self.get_object(pk), data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def patch(self, request, pk):
        serializer = AnswerSerializer(self.get_object(pk), data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        self.get_object(pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)