from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import AppfileForm



# Create your views here.
def Home_page(request):
    return render(request, 'pages/Home.html')

def List(request):
    return render(request, 'pages/3D_list.html')

def submitted(request):
    return render(request, 'pages/upload_list.html')

def upload(request):
    if request.method == 'POST':
     form = AppfileForm(request.POST, request.FILES)
     if form.is_valid():
        form.save()
        return redirect('submitted')
    else:
        form = AppfileForm()
    return render(request, 'pages/Upload_file.html',{
           'form':form
    })




 
  
def model_01(request):
    return render(request, '3D_models/Model_01.html')
def model_02(request):
    return render(request, '3D_models/Model_02.html')
def model_03(request):
    return render(request, '3D_models/Model_03.html')
def model_04(request):
    return render(request, '3D_models/Model_04.html')
def model_05(request):
    return render(request, '3D_models/Model_05.html')
def model_06(request):
    return render(request, '3D_models/Model_06.html')
def model_07(request):
    return render(request, '3D_models/Model_07.html')
def model_08(request):
    return render(request, '3D_models/Model_08.html')
def model_09(request):
    return render(request, '3D_models/Model_09.html')
def model_10(request):
    return render(request, '3D_models/Model_10.html')
def model_11(request):
    return render(request, '3D_models/Model_11.html')
def model_12(request):
    return render(request, '3D_models/Model_12.html')
