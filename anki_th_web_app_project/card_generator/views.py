from django.shortcuts import render

# Create your views here.

#from .models import Post

from django.http import HttpResponse

def home_page(request):
    # return HttpResponse("w")
    return render(request, "card_generator/home.html")

def guide_page(request):
    # return HttpResponse("w")
    return render(request, "card_generator/guide.html")

def try_it_page(request):
    # return HttpResponse("w")
    return render(request, "card_generator/try_it.html")

def shared_deck_page(request):
    # return HttpResponse("w")
    return render(request, "card_generator/shared_deck.html")