from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^tteq_milk', views.total_teq, name='tteq_milk'),
]
