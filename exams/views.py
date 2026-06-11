from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser  # ← add this
from django.shortcuts import get_object_or_404
from django.db import transaction

from .models import Exam, Passage, Question, Answer
from .serializers import (
    ExamSerializer,
    ExamDetailSerializer,
    ExamBulkUploadSerializer,
    PassageSerializer,
    QuestionSerializer,
    AnswerSerializer,
)


# ── Exam ──────────────────────────────────────────────────────────────────────

class ExamListAPIView(APIView):
    def get(self, request):
        exams = Exam.objects.all().order_by('-id')
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
        return Response(ExamDetailSerializer(self.get_object(pk)).data)

    def put(self, request, pk):
        serializer = ExamDetailSerializer(self.get_object(pk), data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def patch(self, request, pk):
        serializer = ExamDetailSerializer(self.get_object(pk), data=request.data, partial=True)
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


# ── Passage ───────────────────────────────────────────────────────────────────

class PassageListAPIView(APIView):
    parser_classes = [MultiPartParser, FormParser]  # ← add this

    def get(self, request):
        passages = Passage.objects.all().order_by('-id')
        return Response(PassageSerializer(passages, many=True).data)

    def post(self, request):
        serializer = PassageSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class PassageDetailAPIView(APIView):
    parser_classes = [MultiPartParser, FormParser]  # ← add this

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
        qs = Question.objects.select_related('passage').prefetch_related('answers').order_by('-id')
        return Response(QuestionSerializer(qs, many=True).data)

    def post(self, request):
        serializer = QuestionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class QuestionDetailAPIView(APIView):
    def get_object(self, pk):
        return get_object_or_404(Question.objects.prefetch_related('answers'), pk=pk)

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
        return Response(AnswerSerializer(Answer.objects.all().order_by('-id'), many=True).data)

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