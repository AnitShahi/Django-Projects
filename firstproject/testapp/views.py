from django.shortcuts import render
from django.http import HttpResponse 
from django.template import loader

def grettings(request):
    s="<h1> hello and welcome to first views</h1>"
    return HttpResponse(s)



def about(request):
    text="Anit"
    template=loader.get_template('about.html')
    context={'text':text}
    res=template.render(context,request)
    return HttpResponse(res)



def contact(request):
    s="<h1> contact page</h1>"
    return HttpResponse(s)


# Create your views here.