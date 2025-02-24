from django.core import serializers
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render,redirect
from django.urls import reverse
from . import models

# Create your views here.

def list(request):
    all_cars= models.Car.objects.all()
    context = {'all_cars': all_cars}
    return render(request,'cars/list.html',context=context)

def add(request):
    if request.method == 'POST':
        brand= request.POST['brand']
        year= int(request.POST['year'])
        models.Car.objects.create(brand=brand, year=year)
        # new_car.save()
        return redirect(reverse('cars:list'))
    # return render(request,'cars/add.html')
    else:
        return render(request,'cars/add.html')
def delete(request):
    if request.method == 'POST':
        pk =request.POST['pk']
        try:
            models.Car.objects.get(pk=pk).delete()
            return redirect(reverse('cars:list'))
        except:
            print('pk not found')
            return redirect(reverse('cars:list'))
    else:
        return render(request,'cars/delete.html')    

    # if request.method == 'POST':
    #     car_id= int(request.POST['car_id'])
    #     models.Car.objects.filter(id=car_id).delete()
    #     return redirect(reverse('cars:list'))
    # return render(request,'cars/delete.html')

# def fetch_car(request,id):
#     car = models.Car.objects.get(id=id)
#     # return HttpResponse(json.dumps(car),content_type='application/json')
#     return JsonResponse(car,content_type='application/json')
#     # return {'car': car}
    

def fetch_car(request, id):
    car_qs = models.Car.objects.filter(id=id)
    if car_qs.exists():
        car_json = serializers.serialize('json', car_qs)
        return HttpResponse(car_json, content_type='application/json')
    else:
        return JsonResponse({'error': 'No data found for the passed id'}, status=404)