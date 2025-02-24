from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def simple_view(request):
    return render(request, 'first_app/example.html')

def variable_view(request):
    my_var={'first_name': 'Daniel', 'last_name': 'Mark'}
    return render(request, 'first_app/variable.html', context=my_var)