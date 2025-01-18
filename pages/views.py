from django.shortcuts import render

def home_view(request):
    return render(request, 'pages/home.html')

def about_view(request):
    return render(request, 'pages/about.html')

def contact_view(request):  
    return render(request, 'pages/contact.html')

def experience_view(request):
    return render(request, 'pages/experience.html')
