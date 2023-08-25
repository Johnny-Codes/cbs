from django.shortcuts import render

from django.http import JsonResponse, HttpResponse

from accounts.models import User, Business
from accounts.serializers import UserSerializer, BusinessSerializer

from rest_framework.response import Response
from rest_framework import mixins, generics
from rest_framework import status


# class UserListApi(APIView):
#     def get(self, request):
#         users = User.objects.all()
#         serializer = UserSerializer(users, many=True)
#         return Response(serializer.data)


# @api_view(["GET", "POST"])
# def user_list_api(request):
#     if request.method == "GET":
#         users = User.objects.all()
#         serializer = UserSerializer(users, many=True)
#         # return JsonResponse(serializer.data, safe=False)
#         return Response(serializer.data)


# @csrf_exempt
# def user_detail_api(request, id):
#     if request.method == "GET":
#         user = User.objects.filter(id=id)
#         serializer = UserSerializer(user, many=True)
#         return JsonResponse(serializer.data, safe=False)
#     elif request.method == "POST":
#         data = JSONParser().parse(request)
#         serializer = UserSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)


class BusinessListView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView,
):
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


# @csrf_exempt
# def business_detail_api(request, id):
#     if request.method == "GET":
#         business = Business.objects.filter(id=id)
#         serializer = BusinessSerializer(business, many=True)
#         return JsonResponse(serializer.data, safe=False)
#     elif request.method == "POST":
#         data = JSONParser().parse(request)
#         serializer = BusinessSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)
#     elif request.method == "PUT":
#         data = JSONParser().parse(request)
#         serializer = BusinessSerializer(business, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)


# @csrf_exempt
# def employees_of_business_api(request, id):
#     employees = User.objects.all().filter(business=id)
#     serializer = UserSerializer(employees, many=True)
#     return JsonResponse(serializer.data, safe=False)
