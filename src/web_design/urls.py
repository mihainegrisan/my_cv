from django.urls import path
from .views import (web_design_view,
                    photo_view,
                    chef_view,
                    barber_view)

app_name = 'web_design'

urlpatterns = [
    path('', web_design_view, name='home'),
    path('photo/', photo_view, name='photo'),
    path('chef/', chef_view, name='chef'),
    path('barber/', barber_view, name='barber'),
]
