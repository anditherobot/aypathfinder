from django.db import models
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, View, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from ayregistration.models import RegistrantInfo, RegistrationCheckList
import logging
logger = logging.getLogger(__name__)

# Create your views here.

def dashboard_home(request):
    return render(request, 'dashboard/index.html')
    ##Sreturn HttpResponse("status=201")

class RegistrantsView(LoginRequiredMixin, ListView):
    model = RegistrantInfo
    context_object_name = 'registrants_list'
    
    template_name = 'dashboard/registrants.html'

class CheckListsView(View):
    def get(self, request):
        checklists_count = RegistrationCheckList.objects.count()
        checklists = RegistrationCheckList.object.all()


class RegistrantsDetails(LoginRequiredMixin, DetailView):
    model = RegistrantInfo
    template_name = 'dashboard/registrantinfo_detail.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)


class dashboard_checklists:
    pass