from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, AnonymousUser
from django.views import View
from django.http.request import *
from django.http.response import *
from django.contrib.auth import authenticate, login, logout

from webapp.forms import LoginForm
from .models import *


# Create your views here.


def index(request: HttpRequest):
    # page = int(request.GET.get('page', 1))
    # begin = 8 * (page-1)
    # end = 8 * page
    # products = Product.objects.all().order_by('id')[begin:end]
    # count = Product.objects.count()
    # context = {'products': products}
    # if page > 1:
    #     context['prev_page'] = page - 1
    # if end < count:
    #     context['next_page'] = page + 1
    # return render(request, 'index.html', context)
## Кнопки физически

    products = Product.objects.all().order_by('id')[:6]
    context = {'products': products}
    return render(request, 'index.html', context)
## кнопка REST API

def product(request: HttpRequest, product_id: int):
    try:
        product = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        return HttpResponseNotFound()
    return render(request, 'product.html', {'product': product})


class LoginView(View):
    def get(self, request: HttpRequest):
        return render(request, 'login.html')

    def post(self, request: HttpRequest):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is None:
            return render(request, 'login.html')
        login(request, user)
        return redirect('/')


class RegisterView(View):
    def get(self, request: HttpRequest):
        return render(request, 'register.html')

    def post(self, request: HttpRequest):
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.create_user(username=username, password=password)
        except:
            return render(request, 'register.html')
        login(request, user)
        return redirect('/')


class Cart(View):
    def get(self, request: HttpRequest):
        return render(request, 'index.html')

    def post(self, request: HttpRequest):
        product = int(request.POST['id'])
        quantity = int(request.POST['quantity'])
        user: User = request.user
        try:
            profile = user.profile
        except User.profile.RelatedObjectDoesNotExist:
            profile = Profile.objects.create(user=user)
        CartItem.objects.create(product_id=product, quantity=quantity, profile=profile)
        return redirect('/')


class TestView(View):

    def get(self, request: HttpRequest):
        return render(request, 'Test_Forms.html', {'form': LoginForm()})

    def post(self, request: HttpRequest):
        form = LoginForm(request.POST)
        if not form.is__valid():
            return HttpResponse(b'error')
        else:
            return HttpResponse(form.cleaned_data['username'])


class ShoppingCart(View):

    def get(self, request: HttpRequest):
        products = Product.objects.all()
        carts = CartItem.objects.all()
        return render(request, 'cart.html', {'products': products, 'carts': carts})
