from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from user.models import User, UserForm


def home(request):
    users = User.objects.all()
    return render(request, 'data.html')


def data(request):
    form = UserForm()
    context = {"form": form}
    return render(request, 'data.html', context)
