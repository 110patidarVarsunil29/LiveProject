from django.shortcuts import render, redirect
from .forms import EmployeeForm, LoginForm
from .models import Employee
from django.contrib.auth.models import auth
from django.contrib import messages

def employee_list(request):
    context = {'employee_list': Employee.objects.all()}
    return render(request, "employee_register/employee_list.html", context)


def employee_form(request,id=0):
    if request.method == "GET":
        if id==0:
            form = EmployeeForm()
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(instance=employee)
        return render(request, "employee_register/employee_form.html", {'form': form})
    else:
        if id==0 :
            form = EmployeeForm(request.POST)
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('/employee/list')


def employee_delete(request, id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('/employee/list')


def login(request):
    if request.method == "POST":
        # #form = LoginForm(data=request.POST)
        # if form.is_valid():
        #     return redirect('/employee/list')
        email = request.POST['email']
        password = request.POST['password']

        usrs = auth.authenticate(email=email, password=password)
        print(usrs)
        if usrs is not None:
            auth.login(request,usrs)
            return redirect("/employee/list")
        else:
            messages.info(request, 'Invalid credentials')
            return redirect("/employee/login")
    else:
        form = LoginForm()
    return render(request, "employee_register/login.html", {'form': form})