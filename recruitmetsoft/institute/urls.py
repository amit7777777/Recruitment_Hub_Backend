from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('',views.read_db,name='read_db'),
    path('get_institute/',views.get_institutes,name='get_institute'),
    path('add_institute/',views.add_institute,name='add_institute'),
    
]