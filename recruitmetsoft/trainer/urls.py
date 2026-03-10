from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',views.read_db,name='read_db'),
    path('get_trainer/',views.get_candidates,name='get_trainer'),
    path('add_trainer/',views.add_candidate,name='add_trainer'),
    
]