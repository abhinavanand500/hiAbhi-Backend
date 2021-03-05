from django.shortcuts import render
from . import urls
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from .models import *
from django.http import HttpResponse, JsonResponse
import json
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
            return JsonResponse({'status': 'success'})
        except:
            return JsonResponse({'status': 'error'})
    return JsonResponse({'status': 'GET REQUEST'})