from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .models import Perro
from django.shortcuts import render



class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

def Galeria(request):
    perros = Perro.objects.all()
    return render(request,'galeria.html',{'perros':perros})
