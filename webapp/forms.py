from django.forms import *
from django.contrib.auth.models import User


class LoginForm(Form):
    username = CharField(max_length=12, min_length=2, validators=[User.username_validator])
    password = CharField(min_length=2, widget=PasswordInput())
