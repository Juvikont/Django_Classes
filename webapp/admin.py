from django.contrib import admin
from webapp.models import *

# Register your models here.

admin.site.register(Product)
admin.site.register(Profile)
admin.site.register(Currency)
admin.site.register(CartItem)