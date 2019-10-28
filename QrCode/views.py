from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.template.context_processors import request


def my_app(request):
    return render(request, 'home.html')


def view_article(request, article_id):
    text = "Displaying article Number : %s" % article_id
    return HttpResponse(text)
