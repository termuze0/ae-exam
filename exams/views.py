from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Exam
from .serializers import (
    ExamSerializer,
    ExamDetailSerializer
)


class ExamListAPIView(APIView):

    def get(self, request):
        exams = Exam.objects.all().order_by('-id')

        serializer = ExamSerializer(
            exams,
            many=True
        )

        return Response(serializer.data)


class ExamDetailAPIView(APIView):

    def get(self, request, pk):
        exam = Exam.objects.get(pk=pk)

        serializer = ExamDetailSerializer(exam)

        return Response(serializer.data)