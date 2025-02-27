import io
from django.shortcuts import get_object_or_404, render
from requests import request
from rest_framework import serializers
from .models import Student
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, HttpResponseBadRequest
from rest_framework.views import APIView

from .serializers import StudentSerializer
from django.views.decorators.csrf import csrf_exempt


class StudentAPIView(APIView):
    def get(self, request, pk=None, format=None):
        if pk is not None:
            
            student = get_object_or_404(Student, id=pk)
            serializer = StudentSerializer(student)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type="application/json")
        
        # If no pk is provided, return all students
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type="application/json")


    

    @csrf_exempt
    def post(self, request, format=None):
        # Get the raw request body (in bytes)
        json_data = request.body
        if not json_data:
            res = {"error": "No data provided"}
            rendered = JSONRenderer().render(res)
            return HttpResponse(rendered, content_type="application/json", status=400)
        
        # Wrap the bytes in a BytesIO stream and parse the JSON
        stream = io.BytesIO(json_data)
        try:
            pythondata = JSONParser().parse(stream)
        except Exception as e:
            res = {"error": "Invalid JSON data", "details": str(e)}
            rendered = JSONRenderer().render(res)
            return HttpResponse(rendered, content_type="application/json", status=400)
        
        # Initialize the serializer with the parsed data
        serializer = StudentSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data Created'}
            rendered = JSONRenderer().render(res)
            return HttpResponse(rendered, content_type="application/json", status=201)
        else:
            rendered = JSONRenderer().render(serializer.errors)
            return HttpResponse(rendered, content_type="application/json", status=400)
        

    def update():
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id=pythondata.get('id')
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu, data=pythondata,partial=True)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data Updated'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type="application/json")
    
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type="application/json")
        

    def delete():
        json_data= request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id=pythondata.get('id')
        if not id:
            return HttpResponseBadRequest("ID is required")
        else:
            stu = Student.objects.get(id=id)
            stu.delete()
            res = {'msg': 'Data Deleted'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type="application/json")
    
# def post(self, request, format=None):
    #     json_data= request.body
    #     stream = io.BytesIO(json_data)
    #     pythondata = JSONParser().parse(stream)
    #     serializer = StudentSerializer(data=pythondata)
    #     if serializer.is_valid():
    #         serializer.save()
    #         res = {'msg': 'Data Created'}
    #         json_data = JSONRenderer().render(res)
    #         return HttpResponse(json_data, content_type="application/json")
    #     json_data = JSONRenderer().render(serializer.errors)
    #     return HttpResponse(json_data, content_type="application/json")

    # def get(self, request, pk=None, format=None):
    #     id = pk
    #     if id is not None:
    #         stu = Student.objects.get(id=id)
    #         serializer = StudentSerializer(stu)
    #         return Response(serializer.data)
    #     stu = Student.objects.all()
    #     serializer = StudentSerializer(stu, many=True)
    #     return Response(serializer.data)

    # def post(self, request, format=None):
    #     serializer = StudentSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response({'msg': 'Data Created'}, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def put(self, request, pk, format=None):
    #     id = pk
    #     stu = Student.objects.get(pk=id)
    #     serializer = StudentSerializer(stu, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response({'msg': 'Complete Data Updated'})
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def patch(self, request, pk, format=None):
    #     id = pk
    #     stu = Student.objects.get(pk=id)
    #     serializer = StudentSerializer(stu, data=request.data, partial=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response({'msg': 'Partial Data Updated'})
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def delete(self, request, pk, format=None):
    #     id = pk
    #     stu = Student.objects.get(pk=id)
    #     stu.delete()
    #     return Response({'msg': 'Data Deleted'}, status=status.HTTP_204_NO_CONTENT)