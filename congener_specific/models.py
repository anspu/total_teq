from django.db import models
from django.forms import ModelForm

class Input(models.Model):
    feed_intake = models.FloatField(
        verbose_name= '(default = 0.116 kg/day)', default=0.116)
    exposure_time = models.FloatField(
        verbose_name= '(days)', default=0.0)
    c1 = models.FloatField(
        verbose_name= '2,3,7,8-TCDF', default=0.0)
    c2 = models.FloatField(
        verbose_name= '1,2,3,7,8-PeCDF', default=0.0)
    c3 = models.FloatField(
        verbose_name= '2,3,4,7,8-PeCDF', default=0.0)
    c4 = models.FloatField(
        verbose_name= '1,2,3,4,7,8-HxCDF', default=0.0)
    c5 = models.FloatField(
        verbose_name= '1,2,3,6,7,8-HxCDF', default=0.0)
    c6 = models.FloatField(
        verbose_name= '2,3,4,6,7,8-HxCDF', default=0.0)
    c7 = models.FloatField(
        verbose_name= '1,2,3,7,8,9-HxCDF', default=0.0)
    c8 = models.FloatField(
        verbose_name= '1,2,3,4,6,7,8-HpCDF', default=0.0)
    c9 = models.FloatField(
        verbose_name= '1,2,3,4,7,8,9-HpCDF', default=0.0)
    c10 = models.FloatField(
        verbose_name= 'OCDF', default=0.0)
    c11 = models.FloatField(
        verbose_name= '2,3,7,8-TCDD', default=0.0)
    c12 = models.FloatField(
        verbose_name= '1,2,3,7,8-PeCDD', default=0.0)
    c13 = models.FloatField(
        verbose_name= '1,2,3,4,7,8-HxCDD', default=0.0)
    c14 = models.FloatField(
        verbose_name= '1,2,3,6,7,8-HxCDD', default=0.0)
    c15 = models.FloatField(
        verbose_name= '1,2,3,7,8,9-HxCDD', default=0.0)


class InputForm(ModelForm):
    class Meta:
        model = Input
        fields = ['feed_intake','exposure_time','c1','c2','c3','c4','c5','c6','c7','c8','c9','c10','c11','c12','c13','c14','c15']
