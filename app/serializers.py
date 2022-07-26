from rest_framework import serializers
from .models import Classification, Object, Document

class ObjectSerializer(serializers.ModelSerializer):
    classification = serializers.ReadOnlyField(source='classification.id')
    image_url = serializers.ImageField(required=False)


    class Meta:
        model = Object
        fields = ['id', 'name', 'image_url', 'classification', 'order', 'family', 'status', 'distribution', 'habitat', 'population', 'protection']

class ListSerializer(serializers.ModelSerializer):
    classification = serializers.ReadOnlyField(source='classification.id')
    image_url = serializers.ImageField(required=False)

    class Meta:
        model = Object
        fields = ['id', 'name', 'image_url', 'classification']

class ClassificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classification
        fields = ['id', 'name']

class DocumentSerializer(serializers.ModelSerializer):
    file_url = serializers.FileField()

    class Meta:
        model = Document
        fields = ['id', 'name', 'file_url']