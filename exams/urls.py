from django.urls import path

from .views import (
    ExamListAPIView,
    ExamDetailAPIView
)

urlpatterns = [
    path(
        'exam/',
        ExamListAPIView.as_view()
    ),

    path(
        'exam/<int:pk>/',
        ExamDetailAPIView.as_view()
    ),
]