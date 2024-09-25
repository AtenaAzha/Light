from django.shortcuts import render , redirect
from django.views import View
from .forms import EmailForm


# Create your views here.
class LandingPage(View):
    def get(self,request):
        return render(request , 'index.html')
    
class Home(View):
    def get(self , request):
        return render(request , 'index.html')

class Projects(View):
    def get(self , request):
        return render(request , 'project.html')
    
class Managing(View):
    def get(self , request):
        form = EmailForm()
        return render(request , 'managing.html' , {'form':form})
    
class Team(View):
    def get(self , request):
        return render(request , 'service.html')
    
class Processes(View):
    def get(self , request):
        return render(request , 'processes.html')
      

    