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
