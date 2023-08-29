from coins.models.denominations import (
    CoinFamily,
    Denominations,
    CoinTypeName,
)
from coins.models.grading import (
    GradingServices,
    CoinGrades,
)
from coins.models.mints import SelectOneMint
from coins.models.strike import Strike
from coins.serializers.voserializers import (
    CoinFamilySerializer,
    GradingServicesSerializer,
    CoinGradesSerializer,
    SelectMintSerializer,
    CoinStrikeSerializer,
    DenominationSerializer,
    CoinTypeNameSerializer,
)

from rest_framework import mixins, generics


class CoinStrikeSerializer(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView,
):
    queryset = Strike.objects.all()
    serializer_class = CoinStrikeSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class CoinFamilySerializerView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView,
):
    queryset = CoinFamily.objects.all()
    serializer_class = CoinFamilySerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class GradingServicesSerializerView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView,
):
    queryset = GradingServices.objects.all()
    serializer_class = GradingServicesSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class CoinGradesSerializerView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView,
):
    queryset = CoinGrades.objects.all().order_by("grade").reverse()
    serializer_class = CoinGradesSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class SelectMintsSerializerView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView,
):
    queryset = SelectOneMint.objects.all()
    serializer_class = SelectMintSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class DenominationSerializerView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView,
):
    queryset = Denominations.objects.all()
    serializer_class = DenominationSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class CoinTypeNameSerializerView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView,
):
    queryset = CoinTypeName.objects.all()
    serializer_class = CoinTypeNameSerializer

    def get(self, request, *args, **kwargs):
        is_deleted_param = request.query_params.get("is_deleted", None)

        if is_deleted_param is not None:
            if is_deleted_param.lower() == "true":
                self.queryset = self.queryset.filter(is_deleted=True)
            elif is_deleted_param.lower() == "false":
                self.queryset = self.queryset.filter(is_deleted=False)

        return self.list(request, *args, **kwargs)
