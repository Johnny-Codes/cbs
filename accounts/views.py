from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from accounts.models import User, Business
from accounts.serializers import UserSerializer, BusinessSerializer

from rest_framework.views import APIView
from rest_framework.response import Response


class UserListApi(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


@api_view(["GET", "POST"])
def user_list_api(request):
    if request.method == "GET":
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        # return JsonResponse(serializer.data, safe=False)
        return Response(serializer.data)


@csrf_exempt
def user_detail_api(request, id):
    if request.method == "GET":
        user = User.objects.filter(id=id)
        serializer = UserSerializer(user, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def business_list_api(request):
    if request.method == "GET":
        businesses = Business.objects.all()
        serializer = BusinessSerializer(businesses, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = BusinessSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def business_detail_api(request, id):
    if request.method == "GET":
        business = Business.objects.filter(id=id)
        serializer = BusinessSerializer(business, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = BusinessSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = BusinessSerializer(business, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def employees_of_business_api(request, id):
    employees = User.objects.all().filter(business=id)
    serializer = UserSerializer(employees, many=True)
    return JsonResponse(serializer.data, safe=False)
