"""Django_Attempt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import webapp.views
from django.conf.urls.static import static
import Django_Classes.settings
from rest_framework.routers import DefaultRouter
import webapp.rest

router = DefaultRouter()
router.register('products', webapp.rest.ProductViewSet)
router.register('cartitem', webapp.rest.CartViewSet)

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', webapp.views.index, name='index'),
                  path('product/<int:product_id>', webapp.views.product),
                  path('login', webapp.views.LoginView.as_view(), name='login'),
                  path('register', webapp.views.RegisterView.as_view(), name='register'),
                  path('cart', webapp.views.Cart.as_view(), name='cart'),
                  path('test', webapp.views.TestView.as_view(), name='test'),
                  path('shopping', webapp.views.ShoppingCart.as_view(), name='carts'),
                  path('api/', include(router.urls))
              ] + static(Django_Classes.settings.MEDIA_URL, document_root=Django_Classes.settings.MEDIA_ROOT)
