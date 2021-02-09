from django.urls import path
from django.contrib.auth.decorators import login_required


from django.views.generic import TemplateView

from ayregistration.views import *

from ayregistration.forms import *

urlpatterns = [
     path('', index, name='index'),
     path('confirm', confirm, name='confirm'),
    
    #path('parttwo', PartTwo.as_view(), name='parttwo'),
    #path('partthree', PartThree.as_view(), name='partthree'),
    #path('confirm', confirm, name='confirm'),
#
    #path('dashboard/participants/', ParticipantView.as_view(), name='participants-list' ),
    #path('dashboard/participants/<int:pk>',participant_details, name='participants-details' ),
    #path('dashboard/participants/<int:pk>/delete',ParticipantDelete.as_view(), name='participants-delete' ),
    #path('dashboard/participants/<int:pk>/update',ParticipantUpdate.as_view(), name='participant-update' ),
    
   


    #path('accounts/profile/', login_required(profile_self), name='profile'),
    #path('accounts/<str:username>/', profile_others, name='profile_others'),

    # wizard forms
    # python manage.py createsuperuserpython manage.py createsuperuser
]
