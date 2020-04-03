from django.urls import path, include
from . import views

app_name = 'employee_register'
urlpatterns = [
    path('', views.employee_form, name='employee_insert'),
    path('<int:id>/', views.employee_form, name="employee_update"),
    path('list/', views.employee_list, name='employee_list'),
    path('delete/<int:id>/', views.employee_delete, name='employee_delete'),
    path('login/', views.login_request, name='login_request'),
    path('register/', views.register, name='register'),
    path("logout", views.logout_request, name="logout_request"),
]