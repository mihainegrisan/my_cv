from django.shortcuts import render


def home_view(request, *args, **kwargs):

    context = {'section' : 'home'}
    return render(request, 'pages/home.html', context)

def about_view(request, *args, **kwargs):

    context = {'section' : 'about'}
    return render(request, 'pages/about.html', context)

def contact_view(request, *args, **kwargs):

    context = {'section' : 'contact'}
    return render(request, 'pages/contact.html', context)

def survey_view(request, *args, **kwargs):

    context = {'section' : 'survey'}
    return render(request, 'pages/survey.html', context)

def weather_view(request, *args, **kwargs):

    context = {'section' : 'weather'}
    return render(request, 'pages/weather.html', context)

def rock_paper_scissors_view(request, *args, **kwargs):

    context = {'section' : 'rock_paper_scissors'}
    return render(request, 'pages/rock_paper_scissors.html', context)


def music_app_view(request, *args, **kwargs):

    context = {'section' : 'music_app'}
    return render(request, 'pages/music_app.html', context)

def page_animation_view(request, *args, **kwargs):

    context = {'section' : 'page_animation'}
    return render(request, 'pages/page_animation.html', context)
