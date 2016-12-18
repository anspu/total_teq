from django.db import models
from django.forms import ModelForm

class Input(models.Model):
    contamination_level = models.FloatField(
        verbose_name= '(ng/kg feed)', default=0.0)
    feed_intake = models.FloatField(
        verbose_name= '(default = 0.116 kg/day)', default=0.116)
    exposure_time = models.FloatField(
        verbose_name= '(days)', default=0.0)

class InputForm(ModelForm):
    class Meta:
        model = Input
        fields = ['contamination_level','feed_intake','exposure_time']
