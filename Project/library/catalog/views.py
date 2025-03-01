from django.http import HttpResponse
from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre, Language

# Create your views here.
def index(request):
    # test_num=Book.objects.all()
    num_books=Book.objects.all().count()
    num_instances=BookInstance.objects.all().count()
    
    num_instances_avail=BookInstance.objects.filter(status__exact='a').count()
    
    context={
        # 'test_num':test_num,
        'num_books':num_books,
        'num_instances':num_instances,
        'num_instances_avail':num_instances_avail,
    }

    return render(request, 'catalog/index.html',context=context)