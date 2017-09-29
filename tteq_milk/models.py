from django.db import models
from django.forms import ModelForm

class Input(models.Model):
    contamination_level = models.FloatField(
        verbose_name= 'Dioxins (ng TEQ/kg feed)', default=0.0)
    contamination_levelPCB = models.FloatField(
        verbose_name= 'DL-PCBs (ng TEQ/kg feed)', default=0.0)
    feed_intake = models.FloatField(
        verbose_name= 'feed intake (kg dm/day)', default=20)
    exposure_time = models.FloatField(
        verbose_name= 'exposure time (days)', default=0.0)
    depletion_time = models.FloatField(
        verbose_name= 'depletion time (days)', default=100.0)
    milk_production = models.FloatField(
        verbose_name= 'milk production (l/day)', default=25)

  

class InputForm(ModelForm):
    class Meta:
        model = Input
        fields = ['contamination_level','contamination_levelPCB','feed_intake','exposure_time','depletion_time','milk_production']
