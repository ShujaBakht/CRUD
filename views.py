from django.shortcuts import render , redirect, HttpResponseRedirect
from django.http import HttpResponse
from tech.models import Employees
from .serializers import EmployeesSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
# Create your views here. 

def home(request):
    #object Relational Mapping
    emp = Employees.objects.all().order_by('-id')
    
    return render(request,'home.html',{'employess': emp,})


def Add(request):
    if request.method == "POST":
        name= request.POST.get('name')
        email=request.POST.get('email')
        address=request.POST.get('address')
        phone= request.POST.get('phone')
        emp = Employees(
            name  = name,
            email = email,
            address = address,
            phone = phone
        )
        emp.save()
        return redirect('home')
    return redirect (request,'home.html')

def Edit(request):
    emp= Employees.objects.all()
    context ={
    'emp': Employees,
    }
    return redirect ('home')



def Update(request,id):
    if request.method == "POST":
        name= request.POST.get('name')
        email= request.POST.get('email')
        address=request.POST.get('address')
        phone= request.POST.get('phone')
        print(name,email,address)
        emp= Employees(
        id=id,
        name= name,
        email= email,
        address=address,
        phone=phone
        )
        emp.save()
        return redirect('home')
    return render(request,'home.html')

def Delete(request,id):
    emp= Employees.objects.get(id=id)
    emp.delete()

    return redirect('home')

    
 # Here is starting functions for API

# def employess_details(request): 
#     # This is my complex data  
#     emp = Employees.objects.get(id=14)
#     # print (emp)
# # Here i am converting complex to python object
#     serilaizer = EmployeesSerializer( emp)
#     # print (serilaizer)
#     # print (serilaizer.data)
# # Here i am converting object into json 
#     json_data = JSONRenderer().render(serilaizer.data)
#     # print(json_data)
# # Here i am render the data to client 
#     return HttpResponse(json_data,content_type='application/json')

def employess_details(request):
    # Query all employee records
    employees = Employees.objects.all()
    
    # Serialize the list of employees
    serializer = EmployeesSerializer(employees, many=True)
    
    # Convert the serialized data to JSON
    json_data = JSONRenderer().render(serializer.data)
    
    # Return the JSON response to the client
    return HttpResponse(json_data, content_type='application/json')