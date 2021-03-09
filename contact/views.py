from django.shortcuts import render
from . import urls
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from .models import *
from django.http import HttpResponse, JsonResponse
import json
from django.conf import settings 
from django.core.mail import send_mail 
# Create your views here.


def landingPage(request):
    if request.user.is_authenticated:
        feeds = Contact.objects.all().order_by('-sno')
        params = {'feeds': feeds}
        return render(request, 'contact/contact.html', params)
    return render(request, 'Backend/home.html')

@csrf_exempt
def postquery(request):
    if(request.method=="POST"):
        try:
            content = json.loads(request.body)
            data = content['params']
            name = data['name']
            email = data['email']
            phone = data['phone']
            query = data['query']
            contact = Contact(name=name, email=email,phone=phone, query=query)
            contact.save()
            subject = f'Hi {name}, thank you for contacting Abhinav Anand.'
            message = 'Just wait for a while. We will connect with you soon. Thankyou for contacting Abhinav. Have a nice day.'
            email_from = settings.EMAIL_HOST_USER 
            recipient_list = [email] 
            send_mail( subject, message, email_from, recipient_list ) 


            return JsonResponse({'status': 'success'})
        except:
            return JsonResponse({'status': 'error'})
    return JsonResponse({'status': 'GET REQUEST'})