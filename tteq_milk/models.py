from django.db import models
from django.forms import ModelForm

class Input(models.Model):
    contamination_level = models.FloatField(
        verbose_name= 'contamination (ng TEQ/kg feed)', default=0.0)
    feed_intake = models.FloatField(
        verbose_name= 'feed intake (kg feed/day)', default=20)
    exposure_time = models.FloatField(
        verbose_name= 'exposure time (days)', default=0.0)

  

class InputForm(ModelForm):
    class Meta:
        model = Input
        fields = ['contamination_level','feed_intake','exposure_time']