from django.contrib import admin
from django.urls import path, include

from pages.views import home_view, code_view, about_view, contact_view, survey_view

app_name = 'pages'

urlpatterns = [
    path('', home_view, name='home'),
    path('contact/', contact_view, name='contact'),
    path('about/', about_view, name='about'),
    path('code/', code_view, name='code'),
    path('survey/', survey_view, name='survey'),
]
