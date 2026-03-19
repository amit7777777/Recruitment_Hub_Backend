from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('',views.read_db,name='read_db'),
    path('login/', views.trainer_login, name='trainer_login'),
    path('get_trainer/', views.get_trainers, name='get_trainer'),
    path('add_trainer/', views.add_trainer, name='add_trainer'),
    
]
