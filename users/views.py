# Create your views here.
from allauth.account.views import logout
from django.shortcuts import redirect


def custom_logout(request):
    logout(request)
    return redirect('places:index')
