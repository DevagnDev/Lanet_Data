from django import views
from django.urls import reverse, path
from .views import HomeView, TeacherDetailView,ThankYouView,TeacherCreateView,TeacherListView


app_name = 'classroom'

urlpatterns = [
    path('home/',HomeView.as_view(),name='home'),
    path('thank_you/', ThankYouView.as_view(), name='thank_you'),
    # path('contact/', ContactView.as_view(), name='contact'),
    path('create_teacher/', TeacherCreateView.as_view(), name='create_teacher'),
    path('teacher_list/', TeacherListView.as_view(), name='teacher_list'),
    path('teacher/<int:id>/', TeacherDetailView.as_view(), name='teacher_detail'),
]
