from django.shortcuts import render

# Create your views here.

def web_design_view(request):

    return render(request, 'web_design/main.html', {})


def photo_view(request):

    return render(request, 'web_design/photo.html', {})

def chef_view(request):

    return render(request, 'web_design/chef.html', {})

def barber_view(request):

    return render(request, 'web_design/barber.html', {})
