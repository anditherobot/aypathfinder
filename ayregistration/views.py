from django.shortcuts import render, redirect
from datetime import date
from .models import RegistrantInfo
from .forms import RegistrantForm
from django.http import HttpResponse
from django.views.generic.edit import CreateView, FormView
from django.contrib import messages
from django.http import HttpResponseRedirect
import logging
logger = logging.getLogger(__name__)

from django.urls import reverse_lazy
# Create your views here.


       

def index(request):
    if request.method == 'POST':
        form = RegistrantForm(request.POST)
        if  form.is_valid():
            form.save()
            #send email
            logger.info("Form is saved with values", form.cleaned_data)
            messages.info(request, "Info: The form has been filled successfully. Thank you!!!")
            return redirect('confirm')
            
        else:
            messages.error(request, 'The form is invalid.')

        return render(request, 'ayregistration/index.html', {'form': form})

    else:
        form = RegistrantForm()
        return render(request, 'ayregistration/index.html', {'form': form})
    
        


def confirm(request):
    template_name = 'ayregistration/confirm.html'
    title = "Information Submitted Correctly"
   
    context = {'title': title,  }
    return render(request, template_name, context)