from django.shortcuts import render
from customers.models import Customers
from customers.serializers import CustomersSerializer

from rest_framework.response import Response
from rest_framework import mixins, generics
from rest_framework import status


class CustomersSerializerView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView,
):
    queryset = Customers.objects.all().order_by("last_name")
    serializer_class = CustomersSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class OneCustomerSerializerView(
    mixins.UpdateModelMixin,
    generics.GenericAPIView,
):
    queryset = Customers.objects.all()
    serializer_class = CustomersSerializer
    lookup_field = "id"

    def get(self, request, *args, **kwargs):
        customer_instance = self.get_object()
        serializer = self.get_serializer(customer_instance)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        customer_instance = self.get_object()
        serializer = self.get_serializer(
            customer_instance,
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
