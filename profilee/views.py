from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from .forms import ProfileForm
from .models import UserProfile
from django.views.generic import ListView
# Create your views here.
from django.views.generic.edit import CreateView
class CreateProfileView(CreateView):
    template_name = 'profilee/profilee.html'
    model = UserProfile
    fields ='__all__'
    success_url = '/profilee'

class Profile_List(ListView):
    model = UserProfile
    template_name = 'profilee/user_profile.html'
    context_object_name = 'profiles'
