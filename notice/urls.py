from django.urls import path
from notice.views import index

urlpatterns = [
    path('', index)
]
