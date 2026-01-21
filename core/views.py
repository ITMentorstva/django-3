
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseNotAllowed
from django.shortcuts import render

products = {
        "Macbook Air 2025": {
            "price": 2000,
            "description": "This is Macbook Air 2025"
        },
        "Macbook Pro 2025": {
            "price": 2800,
            "description": "This is Macbook Pro 2025"
        },
        "iPhone 16 Pro": {
            "price": 1500,
            "description": "This is iPhone 16 Pro"
        },
        "iPad Pro 2025": {
            "price": 1800,
            "description": "This is iPad Pro 2025"
        },
        "Apple Watch Ultra 2": {
            "price": 900,
            "description": "This is Apple Watch Ultra 2"
        }
    }


def home(request):

    context = {
        "products": products
    }

    return render(request, 'index.html', context)

def about(request):
    return HttpResponse("An error happened while serving this page", status=404)

def product(request, name):

    product = products.get(name)
    if not product:
        return HttpResponseNotFound("Proizvod koji trazite nije pronadjen!")

    context = {
        "product": product
    }

    return render(request, 'product.html', context)

def user(request, userId):
    return HttpResponse(f'This is user {userId}')

def create_product(request):
    return render(request, 'product_create.html')

def save_product(request):

    if request.method != "POST":
        return HttpResponseNotAllowed('This method is not allowed!')

    title = request.POST.get("title")
    price = request.POST.get("price")
    description = request.POST.get("description")

    if not title or not price or not description:
        return HttpResponse("All fields are required", status=400)

    return HttpResponse(f'This is a {title}, {price}, {description}', status=201)