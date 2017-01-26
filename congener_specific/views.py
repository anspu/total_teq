from django.shortcuts import render
from congener_specific.models import InputForm
from congener_specific.compute import main
import os

def congener_specific(request):
    os.chdir(os.path.dirname(__file__))
    result = None
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            form2 = form.save(commit=False)
            result = main(form2.feed_intake, form2.exposure_time,form2.c1, form2.c2,form2.c3, form2.c4,
                          form2.c5, form2.c6,form2.c7, form2.c8,
                          form2.c9, form2.c10,form2.c11, form2.c12,
                          form2.c13, form2.c14, form2.c15)
            result = result.replace('static/', '')
            
    else:
        form = InputForm()
    context = {'form': form,'result': result}
    return render(request,'congener_specific.html', context)

