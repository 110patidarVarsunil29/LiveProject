from django import forms
from .models import Employee


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
            #'empcode': 'Emp. Code',
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
        self.fields['password'].required = False
        #self.fields['empcode'].required = True
        self.fields['email'].required = True
        self.fields['manager'].required = True
        self.fields['department'].required = True
        self.fields['date_of_joining'].required = True


class LoginForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['email', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }
        labels = {
            'email': 'Email',
            'password': 'Password',
        }