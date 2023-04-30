from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string

# Create your views here.
def Msg(request):
    return render(request,'FIRSTAPPLICATION/Msg.html')
    #response=render_to_string('FIRSTAPPLICATION/Msg.html')
    #return HttpResponse(response)