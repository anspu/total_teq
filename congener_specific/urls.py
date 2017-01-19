from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^congener_specific/$', views.congener_specific, name='congener_specific'),
]
