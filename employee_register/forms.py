from .models import Employee
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        widgets = {
            'password': forms.PasswordInput(),
        }
        labels = {
            'fullname': 'Full Name',
            'password': 'Password',
            # 'empcode': 'Emp. Code',
            'mobile': 'Mobile',
            'email': 'Email',
            'manager': 'Manager',
            'department': 'Department',
            'position': 'Position',
            'date_of_joining': 'Date of Joining',

        }

    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = "Select"
        self.fields['department'].empty_label = "Select"
        self.fields['manager'].empty_label = "Select"
        self.fields['password'].required = True
        # self.fields['empcode'].required = True
        self.fields['email'].required = True
        self.fields['manager'].required = True
        self.fields['department'].required = True
        self.fields['date_of_joining'].required = True


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


# class LoginForm(forms.ModelForm):
#     class Meta:
#         model = Employee
#         fields = ['username', 'password']
#         widgets = {
#             'password': forms.PasswordInput(),
#         }
#         labels = {
#             'username': 'Username',
#             'password': 'Password',
#         }
#
#     def __init__(self, *args, **kwargs):
#         super(LoginForm, self).__init__(*args, **kwargs)
#         self.fields['username'].required =True
#         self.fields['password'].required =True
