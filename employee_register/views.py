from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee
from django.contrib.auth.models import auth
from django.contrib import messages
from .forms import NewUserForm


def employee_list(request):
    context = {'employee_list': Employee.objects.all()}
    #context = {'employee_list': Employee.objects.raw('select * from employee_register_Employee')}
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

#
# def login(request):
#     if request.method == "POST":
#         # #form = LoginForm(data=request.POST)
#         # if form.is_valid():
#         #     return redirect('/employee/list')
#         username = request.POST['username']
#         password = request.POST['password']
#         print(username)
#         print(password)
#         ausers = auth.authenticate(username=username, password=password)
#         print(ausers)
#         if ausers is not None:
#             auth.login(request, ausers)
#             return redirect("/employee/list")
#         else:
#             messages.info(request, 'Invalid credentials')
#             return redirect("employee/login")
#     else:
#         #form = LoginForm()
#         return render(request, "employee_register/login.html" ) #, {'form': form})


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            login(request, user)
            return redirect("employee/login")

        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])

            return render(request = request,
                          template_name = "employee_register/register.html",
                          context={"form":form})

    form = NewUserForm
    return render(request = request,
                  template_name = "employee_register/register.html",
                  context={"form":form})


def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("employee/login")


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            print(user)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('employee_register:employee_list')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request = request,
                    template_name = "employee_register/login.html",
                    context={"form":form})