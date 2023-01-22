from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse


def index(request):
    return HttpResponse('Success')


def root_method(request):
    return HttpResponse('Succes')


def another_method(request):
    return redirect('/redirected_route')


def redirected_method(request):
    return JsonResponse(
        {"response": "JSON response from redirected_method", "status": True}
    )
