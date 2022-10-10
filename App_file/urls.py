from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import  settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.Home_page, name='Home'),
    path('3D_list',views.List, name='list'),
    path('upload/',views.upload, name='upload'),
     path('submitted/',views.submitted, name='submitted'),
    path('model_01/',views.model_01, name='Model_01'),
    path('model_02/',views.model_02, name='Model_02'),
    path('model_03/',views.model_03, name='Model_03'),
    path('model_04/',views.model_04, name='Model_04'),
    path('model_05/',views.model_05, name='Model_05'),
    path('model_06/',views.model_06, name='Model_06'),
    path('model_07/',views.model_07, name='Model_07'),
    path('model_08/',views.model_08, name='Model_08'),
    path('model_09/',views.model_09, name='Model_09'),
    path('model_10/',views.model_10, name='Model_10'),
    path('model_11/',views.model_11, name='Model_11'),
    path('model_12/',views.model_12, name='Model_12'),


    
 
] +static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)