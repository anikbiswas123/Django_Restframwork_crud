from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from  ApiView import views

urlpatterns = [
    
    path('',views.person_list.as_view()),
    path('person_detalise/<int:pk>/',views.person_detalise.as_view())
    
]

urlpatterns = format_suffix_patterns(urlpatterns)