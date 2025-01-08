from django.shortcuts import render,redirect
from notice.models import Platform, Status
from notice.forms import PlatformModelForm, StatusModelForm
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
# Views da Plataforma

class NewPlatformCreateView(CreateView):
  model = Platform
  form_class = PlatformModelForm
  template_name = 'cadastro/new_platform.html'
  success_url = '/'

class PlatformUpdateView(UpdateView):
  model = Platform
  form_class = PlatformModelForm
  template_name = 'notice/platform_update.html'
  success_url = '/'

class PlatformDeleteView(DeleteView):
  model = Platform
  template_name = 'notice/platform_delete.html'
  success_url = '/'
  
class PlatformListView(ListView):
  model = Platform
  template_name = 'notice/platform.html'
  context_object_name = 'platforms'
  
# Views do Status

class StatusListView(ListView):
  model = Status
  template_name = 'notice/status.html'
  context_object_name =  'status' 

class NewStatusCreateView(CreateView):
  model = Status
  form_class = StatusModelForm
  template_name = 'cadastro/new_status.html'
  success_url = '/'

class StatusUpdateView(UpdateView):
  model = Status
  form_class = StatusModelForm
  template_name = 'notice/status_update.html'
  success_url = reverse_lazy('status')  

class StatusDeteleView(DeleteView):
  model = Status
  template_name = 'notice/status_delete.html'
  success_url = reverse_lazy('status')
    
def index(request):
  return render(request, 'notice/index.html')