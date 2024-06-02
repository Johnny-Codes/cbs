from django.shortcuts import render
from customers.models import Customer
from customers.serializers import CustomersSerializer

from rest_framework.response import Response
from rest_framework import mixins, generics
from rest_framework import status


class CustomersSerializerView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView,
):
    queryset = Customer.objects.all().order_by("last_name")
    serializer_class = CustomersSerializer

    def get(self, request, *args, **kwargs):
        is_deleted_param = request.query_params.get("is_deleted", None)

        if is_deleted_param is not None:
            if is_deleted_param.lower() == "true":
                self.queryset = self.queryset.filter(is_deleted=True)
            elif is_deleted_param.lower() == "false":
                self.queryset = self.queryset.filter(is_deleted=False)

        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        print("post request data: ", request.data)
        return self.create(request, *args, **kwargs)


class OneCustomerSerializerView(
    mixins.UpdateModelMixin,
    generics.GenericAPIView,
):
    queryset = Customer.objects.all()
    serializer_class = CustomersSerializer
    lookup_field = "id"

    def get(self, request, *args, **kwargs):
        customer_instance = self.get_object()
        serializer = self.get_serializer(customer_instance)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        customer_instance = self.get_object()
        if "toggle_soft_delete" in request.data:
            customer_instance.soft_delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

        serializer = self.get_serializer(
            customer_instance,
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
