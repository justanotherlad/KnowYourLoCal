from rest_framework.serializers import ModelSerializer
from api.models import Resource, Category


class ResourceSerializer(ModelSerializer):
    class Meta:
        model = Resource
        fields = "__all__"


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
