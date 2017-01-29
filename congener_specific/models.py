from django.db import models
from django.forms import ModelForm

class Input(models.Model):
    feed_intake = models.FloatField(
        verbose_name= 'feed intake (kg feed/day)', default=0.116)
    exposure_time = models.FloatField(
        verbose_name= 'exposure time (days)', default=0.0)
    c1 = models.FloatField(
        verbose_name= '1: 2,3,7,8-TCDF', default=0.0)
    c2 = models.FloatField(
        verbose_name= '2: 1,2,3,7,8-PeCDF', default=0.0)
    c3 = models.FloatField(
        verbose_name= '3: 2,3,4,7,8-PeCDF', default=0.0)
    c4 = models.FloatField(
        verbose_name= '4: 1,2,3,4,7,8-HxCDF', default=0.0)
    c5 = models.FloatField(
        verbose_name= '5: 1,2,3,6,7,8-HxCDF', default=0.0)
    c6 = models.FloatField(
        verbose_name= '6: 2,3,4,6,7,8-HxCDF', default=0.0)
    c7 = models.FloatField(
        verbose_name= '7: 1,2,3,7,8,9-HxCDF', default=0.0)
    c8 = models.FloatField(
        verbose_name= '8: 1,2,3,4,6,7,8-HpCDF', default=0.0)
    c9 = models.FloatField(
        verbose_name= '9: 1,2,3,4,7,8,9-HpCDF', default=0.0)
    c10 = models.FloatField(
        verbose_name= '10: OCDF', default=0.0)
    c11 = models.FloatField(
        verbose_name= '11: 2,3,7,8-TCDD', default=0.0)
    c12 = models.FloatField(
        verbose_name= '12: 1,2,3,7,8-PeCDD', default=0.0)
    c13 = models.FloatField(
        verbose_name= '13: 1,2,3,4,7,8-HxCDD', default=0.0)
    c14 = models.FloatField(
        verbose_name= '14: 1,2,3,6,7,8-HxCDD', default=0.0)
    c15 = models.FloatField(
        verbose_name= '15: 1,2,3,7,8,9-HxCDD', default=0.0)
    c16 = models.FloatField(
        verbose_name= '16: 1,2,3,4,6,7,8-HpCDD', default=0.0)
    c17 = models.FloatField(
        verbose_name= '17: 1,2,3,4,6,7,8,9-OCDD', default=0.0)
    c18 = models.FloatField(
        verbose_name= "18: 3,4,4',5-TCB (PCB 81)", default=0.0)
    c19 = models.FloatField(
        verbose_name= "19: 3,3',4,4'-TCB (PCB 77)", default=0.0)
    c20 = models.FloatField(
        verbose_name= "20: 3,3',4,4',5-PeCB (PCB 126)", default=0.0)
    c21 = models.FloatField(
        verbose_name= "21: 3,3',4,4',5,5'-HxCB (PCB 169)", default=0.0)
    c22 = models.FloatField(
        verbose_name= "22: 2',3,4,4',5-PeCB (PCB 123)", default=0.0)
    c23 = models.FloatField(
        verbose_name= "23: 2,3',4,4',5-PeCB (PCB 118)", default=0.0)
    c24 = models.FloatField(
        verbose_name= "24: 2,3,4,4',5-PeCB (PCB 114)", default=0.0)
    c25 = models.FloatField(
        verbose_name= "25: 2,3,3',4,4'-PeCB (PCB 105)", default=0.0)
    c26 = models.FloatField(
        verbose_name= "26: 2,3',4,4',5,5'-HxCB (PCB 167)", default=0.0)
    c27 = models.FloatField(
        verbose_name= "27: 2,3,3',4,4',5'-HxCB (PCB 157)", default=0.0)
    c28 = models.FloatField(
        verbose_name= "28: 2,3,3',4,4',5-HxCB (PCB 156)", default=0.0)
    c29 = models.FloatField(
        verbose_name= "29: 2,3,3',4,4',5,5'-HpCB (PCB 189)", default=0.0)





class InputForm(ModelForm):
    class Meta:
        model = Input
        fields = ['feed_intake','exposure_time','c1','c2','c3','c4','c5','c6','c7','c8','c9','c10','c11','c12','c13','c14','c15','c16','c17','c18','c19','c20','c21','c22','c23','c24','c25','c26','c27','c28','c29',]
