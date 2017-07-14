from django.shortcuts import render
from .models import User


def users(request):
    users = User.objects.all()
    return render(request, 'index.html', {'users': users})