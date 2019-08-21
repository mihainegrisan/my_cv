from django.shortcuts import render


def home_view(request, *args, **kwargs):

    context = {}
    return render(request, 'pages/home.html', context)

def code_view(request, *args, **kwargs):

    context = {}
    return render(request, 'pages/code.html', context)

def about_view(request, *args, **kwargs):

    context = {}
    return render(request, 'pages/about.html', context)

def contact_view(request, *args, **kwargs):

    context = {}
    return render(request, 'pages/contact.html', context)

def survey_view(request, *args, **kwargs):

    context = {}
    return render(request, 'pages/survey.html', context)
