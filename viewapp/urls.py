
from django.urls import path
from django.urls.conf import include
from viewapp import views
from viewapp.views import emloyeeViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('emloyeeViewSet', emloyeeViewSet, basename='emloyeeViewSet')


urlpatterns =[
    path('',include(router.urls))
]

