
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',include('app.urls')),
    # path('',include('app1.urls')),
    # path('',include('restapp.urls')),
    # path('',include('ApiView.urls')),
    # path('',include('classApp.urls')),
    # path('',include('minixapp.urls')),
    path('',include('viewapp.urls')),
]
