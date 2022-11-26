from django.http import HttpResponse
from django.shortcuts import render
from service.models import User

n = 0


def home(request):
    users = User.objects.all()
    user = users[n]
    return render(request, 'index.html', {'user': user})


def profile(request, pid):
    users = User.objects.all()
    user = users.get(id=int(pid))
    return render(request, 'profile.html', {'user': user})
