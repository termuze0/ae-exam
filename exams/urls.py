from django.urls import path
from .views import (
    ExamListAPIView,
    ExamDetailAPIView,
    ExamBulkUploadAPIView,
    PassageListAPIView,
    PassageDetailAPIView,
    QuestionListAPIView,
    QuestionDetailAPIView,
    AnswerListAPIView,
    AnswerDetailAPIView,
)
urlpatterns = [
    # Exam
    path('exams/bulk-upload/',  ExamBulkUploadAPIView.as_view()),  # ← must be before <pk>
    path('exams/',              ExamListAPIView.as_view()),
    path('exams/<int:pk>/',     ExamDetailAPIView.as_view()),

    # Passage
    path('passages/',           PassageListAPIView.as_view()),
    path('passages/<int:pk>/',  PassageDetailAPIView.as_view()),

    # Question
    path('questions/',          QuestionListAPIView.as_view()),
    path('questions/<int:pk>/', QuestionDetailAPIView.as_view()),

    # Answer
    path('answers/',            AnswerListAPIView.as_view()),
    path('answers/<int:pk>/',   AnswerDetailAPIView.as_view()),
]


