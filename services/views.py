from django.shortcuts import get_object_or_404, render
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.core.mail import EmailMessage
from django.conf import settings
from .models import Contact
from .models import Shop
from .models import Services
from .models import Food
from .models import Order
from home.models import SupportStaffDetails
from canteen import settings
# sending sms
from twilio.rest import Client
# Create your views here.


def deliveryForm(request):
    staffDetails = SupportStaffDetails.objects.all()[0]
    staffDetails2 = SupportStaffDetails.objects.all()[1]
    print(staffDetails2.contact)

    if request.method == 'POST':
        try:
            service_shop = request.POST['shop_name']
            name = request.POST['name']
            email = request.POST['email']
            contact = request.POST['contact']
            package = request.POST['food']
            num_of_packs = request.POST['num_of_packs']
            location = request.POST['location']
            address = request.POST['address']
            user_preference = request.POST['user-preference']
        except:
            messages.error(request, "please all fields are required")
            return redirect(deliveryForm)

        # print(service_shop, name, package, location, address,
        #       num_of_packs, contact,  email, user_preference)

        if name and email and package and location and address and num_of_packs and contact:
            message = f"Name: {name} \n emial : {email} \n service_shop: {service_shop}\n package: {package} \n address:{address} \n num_of_pack: {num_of_packs} \n location: {location} \n contact: {contact} \n message: {user_preference}"
            order = Order.objects.create(
                name=name, email=email,  package=package, service_shop=service_shop, location=location, num_of_packs=num_of_packs, address=address, contact=contact, user_preference=user_preference)
            customerGmailMessage = f'Hi {name} , Your {package} order was successful. currently working on your order . Thanks for Using our services'
            try:
                # adminEmail = 'alexanderemmanuel1719@gmail.com'
                adminEmail = staffDetails.email
                deliveryStaff = staffDetails2.email
                subject = 'ALEXIS DELIVERY'

                email_message = EmailMessage(
                    subject,
                    message,
                    settings.EMAIL_HOST_USER,
                    [adminEmail],
                )
                deliveryStaff_message = EmailMessage(
                    subject,
                    message,
                    settings.EMAIL_HOST_USER,
                    [deliveryStaff],
                )
                customerGmail = EmailMessage(
                    subject,
                    customerGmailMessage,
                    settings.EMAIL_HOST_USER,
                    [email]
                )
                is_delivery_email_sent = deliveryStaff_message.send()
                is_customer_email_sent = customerGmail.send()
                is_email_sent = email_message.send()
                account_sid = settings.ACCOUNT_SID
                auth_token = settings.AUTH_TOKEN
                client = Client(account_sid, auth_token)
                # customerMessage = client.messages.create(
                #     body=f'\nHi {name}\n Your {package} order was successful. currently working on your order.\nThanks for using ALEXIS SERVICES.',
                #     from_=settings.TRIAL_NUM,
                #     to=staffDetails2.contact
                # )
                staffMessage = client.messages.create(
                    body=message,
                    from_=settings.TRIAL_NUM,
                    to=staffDetails.contact
                )

                # deliveryMessage = client.messages.create(
                #     body=message,
                #     from_=settings.TRIAL_NUM,
                #     to=staffDetails2.contact
                # )
                # print(deliveryMessage)
                # print(customerMessage.sid)
                print(staffMessage.sid)

                if is_email_sent and is_customer_email_sent:
                    order.save()

                    messages.info(
                        request, f'Hi {name} , Your {package} order was successful. currently working on your order . Thanks for Using our services')

            except:
                messages.warning(
                    request, "Please Try Again, Something Went Wrong. Hint: please kindly check the phone number(FORMAT:+233503843928) or make sure your Email is correct, if the problem still persist check your internet connection")

            finally:
                return redirect('home')

        else:
            messages.warning(
                request, "Please Try Again, Something Went Wrong. Hint: All fields are required")
            return redirect('home')
        #message = request.POST['message']

    else:
       # print("It is not post")
        return render(request, 'university_form.html')


def store(request, services_slug=None):
    staffDetails = SupportStaffDetails.objects.all()[0]
    services = None
    shops = None
    if services_slug != None:
        services = get_object_or_404(Services, slug=services_slug)
        shops = Shop.objects.filter(services=services, is_active=True)
        shop_count = shops.count()
    else:
        shops = Shop.objects.all().filter(is_active=True)
        shop_count = shops.count()

    context = {
        'shops': shops,
        'shop_count': shop_count,
        'staffDetails': staffDetails

    }
    # print(shops)
    # print(shop_count)
    return render(request, 'stores.html', {"context": context})


def delivery(request, service, shop_name):
    #print(shop_name, service)

    staffDetails = SupportStaffDetails.objects.all()[0]
    # if shop_name:
    #     category = service.lower().split('-')
    foods = Food.objects.all()

    context = {"foods": foods,
               "shop_name": shop_name,
               'staffDetails': staffDetails
               }
    return render(request, 'university_form.html', {"context": context})

    # print("printing", category)
    # if 'university' in category:
    #     return render(request, 'university_form.html', {"context": context})
    # elif 'gas' in category:
    #     return render(request, "gas_form.html", {"context": context})

    # return render(request, 'food_delivery.html', {"context": context})


def contact(request):
    if request.method == 'POST':
        try:
            name = request.POST['name']
            email = request.POST['email']
            subject = request.POST['subject']
            message = request.POST['message']
            print(name, email, subject, message)
            message = f"Name: {name} \n emial : {email} \n subject: {subject} \n message: {message}"
            contact_us = Contact.objects.create(
                name=name, email=email,  subject=subject, message=message)
        except:
            messages.warning(
                request, "Please Try Again, Something Went Wrong. Hint: please kindly check your internet connection")
            return redirect('contact')

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
            contact_us.save()
            messages.info(
                request, f'Message sent successfully . Thanks {name} for the contacting us we get to you as soon as possible')
            return redirect('home')
        except:
            messages.warning(
                request, "Please Try Again, Something Went Wrong. Hint: please kindly check your internet connection")
            return redirect('contact')

        # message = request.POST['message']

    else:
       # print("It is not post")
        return render(request, 'contact.html')
