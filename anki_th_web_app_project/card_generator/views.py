from django.shortcuts import render

# Create your views here.

#from .models import Post


import sys 
sys.path.append('../reference')
import ankiTH

from django.shortcuts import redirect

from django.http import HttpResponse

def home_page(request):
    # return HttpResponse("w")
    return render(request, "card_generator/home.html")

def guide_page(request):
    # return HttpResponse("w")
    return render(request, "card_generator/guide.html")

def try_it_page(request):
    # return HttpResponse("w")

    
    for key, value in request.POST.items():
        print('Key: %s' % (key) ) 
        # print(f'Key: {key}') in Python >= 3.7
        print('Value %s' % (value) )
        # print(f'Value: {value}') in Python >= 3.7
    if request.method == 'GET':
        print("welcome to try_it_page")
    elif request.method == 'POST':
        print("post")
    
    return render(request, "card_generator/try_it.html")

def shared_deck_page(request):
    # return HttpResponse("w")
    return render(request, "card_generator/shared_deck.html")

def generate_output(request):
    print("pressed")
    return HttpResponse("w")
    return render(request, "card_generator/try_it.html", {"output_text":"hello"})