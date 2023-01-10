from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Features
from .models import HomePageWords
from services.models import Services
from .models import FrequentQuestion
from .models import Testimonies
from .models import SupportStaffDetails
from django.contrib import messages
from django.core.mail import EmailMessage
from django.conf import settings
# Create your views here.


def home(request):
    features = Features.objects.all()
    homeWords = HomePageWords.objects.all()[0]
    services = Services.objects.all()
    testimonies = Testimonies.objects.all()
    staffDetails = SupportStaffDetails.objects.all()[0]
    # print(staffDetails.location)
    faqs = FrequentQuestion.objects.all().order_by('number')

    context = {'features': features, 'homeWords': homeWords, 'services': services,
               'testimonies': testimonies, "staffDetails": staffDetails, "faqs": faqs}
    return render(request, 'index.html', {'context': context})


# def review(request):
#     return render(request, "reviewForm.html")


def reviewForm(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        job_title = request.POST['job_title']
        rating = request.POST['rating']
        customer_review = request.POST['message']
        print(name, job_title, rating, customer_review)
        if name and email and job_title and rating and customer_review:
            message = f"Name: {name} \n emial : {email} \n job_title: {job_title} \n rating: {rating} \n message: {customer_review}"
            customer_review = Testimonies.objects.create(
                name=name, email=email,  job_title=job_title, rating=rating, customer_review=customer_review)

            adminEmail = 'alexanderemmanuel1719@gmail.com'
            subject = 'ALEXIS DELIVERY'
            email_message = EmailMessage(
                subject,
                message,
                settings.EMAIL_HOST_USER,
                [adminEmail],
            )
            try:
                email_message.send()
                customer_review.save()
                messages.info(
                    request, f'Message sent successfully . Thanks {name} for the review')
                return redirect('home')
            except:
                messages.warning(
                    request, "Please Try Again, Something Went Wrong. Hint: please kindly check your internet connection")
                return render(request, 'reviewForm.html')
        else:
            messages.warning(
                request, "Please Try Again, Something Went Wrong. Hint: All fields are required")
            return render(request, 'reviewForm.html')
        # message = request.POST['message']

    else:
       # print("It is not post")
        return render(request, 'reviewForm.html')
