from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    response = HttpResponse(status=302)
    response['Location'] = '/view/'
    return response
    #return render(request,'/view/login.html')