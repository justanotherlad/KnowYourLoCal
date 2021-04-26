from rest_framework import generics
from api.models import Resource, Category
from api.serializers import ResourceSerializer, CategorySerializer


class ResourceList(generics.ListCreateAPIView):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer

    def get_queryset(self):
        if "lat" in self.request.query_params and "long" in self.request.query_params:
            lat = float(self.request.query_params["lat"])
            long = float(self.request.query_params["long"])
            return Resource.objects.filter(
                lat__gt=lat - 3, lat__lt=lat + 3, long__gt=long - 3, long__lt=long + 3
            )
        else:
            return Resource.objects.all()


class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
