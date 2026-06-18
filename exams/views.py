from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from django.shortcuts import get_object_or_404
from django.db import transaction
from django.contrib.auth.hashers import check_password
from .models import Exam, Passage, Question, Answer, ExamSession, StudentAnswer, ExamResult
from .serializers import (
    ExamSerializer,
    ExamDetailSerializer,
    ExamStudentSerializer,
    ExamBulkUploadSerializer,
    ExamPasswordCheckSerializer,
    PassageSerializer,
    QuestionSerializer,
    AnswerSerializer,
    ExamSubmitSerializer, ExamResultSerializer
)


# ── Exam ──────────────────────────────────────────────────────────────────────

class ExamListAPIView(APIView):
    def get(self, request):
        exams = Exam.objects.filter(is_active=True).order_by("-id")
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
    def post(self, request, pk):
        exam = get_object_or_404(Exam, pk=pk)

        # If exam has no password, skip validation entirely
        if not exam.password:
            return Response(ExamStudentSerializer(exam).data, status=status.HTTP_200_OK)

        serializer = ExamPasswordCheckSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        submitted_password = serializer.validated_data["password"]

        if not check_password(submitted_password, exam.password):
            return Response(
                {"detail": "Incorrect exam password."},
                status=status.HTTP_403_FORBIDDEN,
            )

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
class ExamSubmitAPIView(APIView):
    """
    POST /exams/<pk>/submit/
    Body: { "answers": [{"question_id": 1, "answer_id": 3}, ...] }

    - Creates (or reuses) an ExamSession for the authenticated student.
    - Rejects duplicate submissions with 409.
    - Saves StudentAnswer rows, computes and stores ExamResult.
    """
    def post(self, request, pk):
        exam    = get_object_or_404(Exam, pk=pk)
        student = request.user          # requires authentication middleware

        serializer = ExamSubmitSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        session, created = ExamSession.objects.get_or_create(
            student=student, exam=exam
        )
        if session.submitted:
            return Response(
                {"detail": "You have already submitted this exam."},
                status=status.HTTP_409_CONFLICT,
            )

        with transaction.atomic():
            answers_data = serializer.validated_data["answers"]
            correct_count = 0

            for entry in answers_data:
                question = get_object_or_404(Question, pk=entry["question_id"], exam=exam)
                answer   = None
                if entry.get("answer_id") is not None:
                    answer = get_object_or_404(Answer, pk=entry["answer_id"], question=question)

                student_answer, _ = StudentAnswer.objects.update_or_create(
                    session=session,
                    question=question,
                    defaults={"selected_answer": answer},
                )
                if student_answer.is_correct:
                    correct_count += 1

            total = exam.questions.count()
            passed = (correct_count / total) >= ExamResult.PASS_THRESHOLD if total else False

            ExamResult.objects.create(
                session=session,
                score=correct_count,
                total=total,
                passed=passed,
            )

            session.submitted = True
            session.save()

        result = ExamResult.objects.get(session=session)
        return Response(ExamResultSerializer(result).data, status=status.HTTP_201_CREATED)


class ExamResultAPIView(APIView):
    """
    GET /exams/<pk>/result/
    Returns the stored result for the authenticated student.
    """
    def get(self, request, pk):
        exam    = get_object_or_404(Exam, pk=pk)
        session = get_object_or_404(ExamSession, exam=exam, student=request.user)

        if not session.submitted:
            return Response(
                {"detail": "Exam not submitted yet."},
                status=status.HTTP_404_NOT_FOUND,
            )

        result = get_object_or_404(ExamResult, session=session)
        return Response(ExamResultSerializer(result).data)