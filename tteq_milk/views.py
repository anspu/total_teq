from django.shortcuts import render
from tteq_milk.models import InputForm
from tteq_milk.compute import main
import os

def total_teq(request):
    os.chdir(os.path.dirname(__file__))
    result = None
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            form2 = form.save(commit=False)
            result = main(form2.contamination_level,form2.contamination_levelPCB,form2.feed_intake, form2.exposure_time, form2.depletion_time, form2.milk_production)
            result = result.replace('static/', '')
            
    else:
        form = InputForm()
    context = {'form': form,'result': result}
    return render(request,'tteq_milk.html', context)
