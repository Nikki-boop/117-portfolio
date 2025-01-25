from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail

def home_view(request):
    return render(request, 'pages/home.html')

def about_view(request):
    return render(request, 'pages/about.html')

def contact_view(request):
    if request.method == "POST":
        print("sending email")
        form = ContactForm(request.POST)
        if form.is_valid():
            print("form is valid")

            message = form.cleaned_data['message']
   
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']

            message_body = f"This is an email from your page. \nName: {name}\nEmail: {email}\nMessage: {message}"

            send_mail(
                "Portfolio Email",
                message_body,
                email,
                ['sinzunza@sdgku.edu']
            )

            
            return render(request, 'pages/contact.html', {'form': form, "success": True})

        else: 
            print("form is not valid")
    else:
        form = ContactForm()

    return render(request, 'pages/contact.html', {'form': form})



def projects_view(request):
    return render(request, 'pages/projects.html')
