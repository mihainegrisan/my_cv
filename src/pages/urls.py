from django.contrib import admin
from django.urls import path, include
from pages.views import (home_view,
                         about_view,
                         contact_view,
                         survey_view,
                         weather_view,
                         rock_paper_scissors_view,
                         music_app_view,
                         page_animation_view)

app_name = 'pages'

urlpatterns = [
    path('', home_view, name='home'),
    path('contact/', contact_view, name='contact'),
    path('about/', about_view, name='about'),
    path('survey/', survey_view, name='survey'),
    path('weather/', weather_view, name='weather'),
    path('rock_paper_scissors/', rock_paper_scissors_view, name='rock_paper_scissors'),
    path('music_app/', music_app_view, name='music_app'),
    path('page_animation/', page_animation_view, name='page_animation'),

]
