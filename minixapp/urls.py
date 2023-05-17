from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from  minixapp import views

urlpatterns = [
    
    # path('',views.employeeList.as_view()),
    # path('EmployeeDetail/<int:pk>/',views.EmployeeDetail.as_view())
    
    
]

urlpatterns = format_suffix_patterns(urlpatterns)