from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def fourzerofour(request):
    return render(request, '404.html')


def cart(request):
    return render(request, 'cart.html')


def chackout(request):
    return render(request, 'chackout.html')


def contact(request):
    return render(request, 'contact.html')

def shopdetail(request):
    return render(request, 'shop-detail.html')

def shop(request):
    return render(request, 'shop.html')

def testimonial(request):

    return render(request, 'testimonial.html')

# Create your views here.
