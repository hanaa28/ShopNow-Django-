from django.shortcuts import render,redirect,reverse
from django.contrib.auth.forms import authenticate
from django.contrib.auth.models import User
from category.models import *
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

# def mylogin(request):
#     context={'form': authenticate()}
#     return render(request, 'registration/login.html', context)

def myprofile(request):
    r=reverse('category_list')
    return redirect(r)
class myregister(CreateView):
    model=User
    template_name='registration/registration.html'
    form_class=UserCreationForm
    context_object_name='form'
    success_url=reverse_lazy('login')

 