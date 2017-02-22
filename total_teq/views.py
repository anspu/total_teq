from django.shortcuts import render
from total_teq.models import InputForm
from total_teq.compute import main
from django.views.generic import ListView
from total_teq.models import Feedregime
import os

class Feed_Regimes(ListView):
        model = Feedregime

def total_teq(request):
    os.chdir(os.path.dirname(__file__))
    result = None
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            form2 = form.save(commit=False)
            result = main(form2.contamination_level, form2.feed_intake, form2.exposure_time)
            result = result.replace('static/', '')
            
    else:
        form = InputForm()
    context = {'form': form,'result': result}
    return render(request,'total_teq.html', context)
