from django.db import models
from django.forms import ModelForm

class Input(models.Model):
    contamination_level = models.FloatField(
        verbose_name= 'Dioxins (ng TEQ/kg feed)', default=0.0)
    contamination_levelPCB = models.FloatField(
        verbose_name= 'DL-PCBs (ng TEQ/kg feed)', default=0.0)
    feed_intake = models.FloatField(
        verbose_name= 'feed intake (kg dm/day)', default=0.116)
    exposure_time = models.FloatField(
        verbose_name= 'exposure time (days)', default=0.0)
    depletion_time = models.FloatField(
        verbose_name= 'depletion time (days)', default=0.0)


class InputForm(ModelForm):
    class Meta:
        model = Input
        fields = ['contamination_level','contamination_levelPCB','feed_intake','exposure_time','depletion_time']

        #http://www.ilian.io/django-forms-choicefield-with-dynamic-values/
 
class Feedregime(models.Model):
    feed_regime = models.CharField(max_length=200)
    animal = models.CharField(max_length=200)

    def __str__(self):
        return self.feed_regime + ' - ' + self.animal

class Ingredients(models.Model):
    feed_regime = models.ForeignKey(Feedregime,on_delete=models.CASCADE)
    ingredient = models.CharField(max_length=200)
    amount = models.FloatField()

    def __str__(self):
     return self.ingredient
  



