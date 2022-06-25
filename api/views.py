from functools import partial
import json
from django.shortcuts import render
import io 
from rest_framework.parsers import JSONParser
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
 
# Create your views here.

@csrf_exempt
def student_api(request):

# Inser Data Into Database 
    
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = StudentSerializer(data = pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {'msg' : 'Data Created'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')



#  Read Data 

    if request.method == 'GET':
        json_data = request.body    # JSON Data Get From Client side
        stream = io.BytesIO(json_data)    # DATA Stream 
        pythondata = JSONParser().parse(stream)  # JSON convert Into Python Data
        id = pythondata.get('id', None)   # ID Match or Full Data Post
        if id is not None: # If Id Match
            stud = Student.objects.get(id=id)  # Get ID Related Data
            serializer = StudentSerializer(stud) # Complex Data (SQL) convert into Python 
            json_data = JSONRenderer().render(serializer.data) # Reender Data into JSON and send back to client sie=de
            return HttpResponse(json_data, content_type='application/json')
        
        stud = Student.objects.all() # If Id is not NOne The provide all data
        serializer = StudentSerializer(stud, many=True) # SQL into python
        json_data = JSONRenderer().render(serializer.data) # provide data into JSON formate 
        return HttpResponse(json_data, content_type='application/jsos')

#  Update data 

    if request.method == 'PUT':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        stud = Student.objects.get(id = id)

        #Full data Update = Required All Data From Front End
        # Serializer = StudentSerializer(stud, data=pythondata)
        # Partial Update = All Data Not Required

        serializer = StudentSerializer(stud, data=pythondata, partial= True)
        
        if serializer.is_valid():
            serializer.save()
            res = {'msg' : 'Data Has Been Updated'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type = 'application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type = 'application/json')


    if request.method == 'DELETE':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        stud = Student.objects.get(id = id)
        stud.delete()
        res = {'msg' : 'Data Has Been Deleted--'}
        # json_data = JSONRenderer().render(res)
        # return HttpResponse(json_data, content_type = 'application/json')
        return JsonResponse(res, safe=False)

