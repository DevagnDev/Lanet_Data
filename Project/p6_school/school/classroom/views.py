from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView,FormView,CreateView, ListView
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from classroom.models import Teacher 

# Create your views here.
# def home_view(request):
#     return render(request, 'classroom/home.html')


class HomeView(TemplateView):
    template_name = 'classroom/home.html'

class ThankYouView(TemplateView):
    template_name = 'classroom/thank_you.html'

class TeacherCreateView(CreateView):
    model = Teacher
    fields = "__all__"
    success_url = reverse_lazy('classroom:thank_you')

class TeacherListView(ListView):
    model = Teacher
    context_object_name = 'teacher_list'
     
class ContactView(TemplateView):
    template_name = 'classroom/contact.html'


# class teacher_detail(ListView,id):
#     model=Teacher
#     teacher = get_object_or_404(model, id=id)
#     data = {
#         "first_name": teacher.first_name,
#         "last_name": teacher.last_name,
#         "subject": teacher.subject,
#     }
#     def __init__(self, data):
#         return JsonResponse(data)
    

class TeacherDetailView(View):
    def get(self, request, id, *args, **kwargs):
        teacher = get_object_or_404(Teacher, id=id)
        data = {
            "first_name": teacher.first_name,
            "last_name": teacher.last_name,
            "subject": teacher.subject,
        }
        return JsonResponse(data)