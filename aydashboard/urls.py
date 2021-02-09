from django.urls import path
from django.contrib.auth.decorators import login_required


from django.views.generic import TemplateView

from aydashboard.views import *
from .api_routes import *
urlpatterns = [
    path('home/', dashboard_home, name='dashboard_home'),
    path('checklists', dashboard_checklists, name='dashboard_checklists'),
    path('registrants/', RegistrantsView.as_view(), name='registrants-list' ),
    #path('api/', include(router.urls)),
    path('dashboard/registrants/<int:pk>',RegistrantsDetails.as_view(), name='registrants-details' ),
   # path('dashboard/participants/<int:pk>/delete',ParticipantDelete.as_view(), name='participants-delete' ),
    #path('dashboard/participants/<int:pk>/update',ParticipantUpdate.as_view(), name='participant-update' ),


    #path('accounts/profile/', login_required(profile_self), name='profile'),
    #path('accounts/<str:username>/', profile_others, name='profile_others'),

    # wizard forms
    # python manage.py createsuperuserpython manage.py createsuperuser
]
