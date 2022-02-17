from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages

from .models import User, UserForm
from django.forms.models import model_to_dict


@csrf_exempt
def user(request):
    if request.method == "POST":
        form = UserForm(request.POST)

        if form.is_valid():
            new_user = form.save()
            return JsonResponse({
                'success': True,
                'data': model_to_dict(new_user)
            }, safe=False)
        else:
            return JsonResponse({
                'success': False,
                'errors': dict(form.errors.items()),
            })
