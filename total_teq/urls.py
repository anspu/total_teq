from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^total_teq', views.total_teq, name='total_teq'),
]
