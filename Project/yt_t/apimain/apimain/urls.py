from django.urls import path
from api.views import StudentAPIView

urlpatterns = [
    path('studentapi/', StudentAPIView.as_view(), name='student_api'),
    path('studentapi/<int:pk>/', StudentAPIView.as_view(), name='student_api_detail'),
    # path('studentapi/', StudentAPIView, name='student_api'),
]