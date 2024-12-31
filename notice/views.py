from django.shortcuts import render,redirect
from notice.models import Platform, Status
from notice.forms import PlatformModelForm, StatusModelForm
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

class PlatformUpdateView(UpdateView):
  model = Platform
  form_class = PlatformModelForm
  template_name = 'notice/platform_update.html'
  success_url = '/'

class NewPlatformCreateView(CreateView):
  model = Platform
  form_class = PlatformModelForm
  template_name = 'cadastro/new_platform.html'
  success_url = '/'

class NewStatusCreateView(CreateView):
  model = Status
  form_class = StatusModelForm
  template_name = 'cadastro/new_status.html'
  success_url = '/'

class PlatformListView(ListView):
  model = Platform
  template_name = 'notice/platform.html'
  context_object_name = 'platforms'
  
  
  
def index(request):
  return render(request, 'notice/index.html')