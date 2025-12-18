from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from main.models import Apartment, Object
from .serializers import ApartmentSerializer, ObjectSerializer, ApartmentCreateUpdateSerilizer
from .pagination import StandartResultPagination
from django_filters.rest_framework import DjangoFilterBackend

class ApartmentViewSet(ModelViewSet):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer
    permission_classes = (AllowAny,)
    pagination_class = StandartResultPagination
    
    filter_backends = (DjangoFilterBackend)
    filterset_fields = ('type', 'rooms_count', 'floor', 'area', 'price', 'object__name')
    filterset_fields = {('price', 'area'): ['gte', 'lte']}


    def get_serializer_class(self):
        if self.action == "retireve":
            return ApartmentCreateUpdateSerilizer
        elif self.action in ["create", "update", "partial_update"]:
            return ApartmentCreateUpdateSerilizer
        return super().get_serializer_class()
    
    def get_permissions(self):
        if self.action in ["create", "update", "partial_update", "delete"]:
            return IsAdminUser
        return super().get_permissions()


class ObjectViewSet(ReadOnlyModelViewSet):
    queryset = Object.objects.all()
    serializer_class = ObjectSerializer
    