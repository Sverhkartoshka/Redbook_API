from msilib.schema import Class
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Classification, Object, Document
from .serializers import ClassificationSerializer, ObjectSerializer, ListSerializer, DocumentSerializer
from rest_framework import permissions
from rest_framework.parsers import MultiPartParser, FormParser, FileUploadParser

class ObjectView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

    def get(self, request, pk):
        q = Object.objects.all()
        req = get_object_or_404(q, pk=pk)
        serializer = ObjectSerializer(req)
        return Response(serializer.data)

class ListView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

    def get(self, request, classification):
        q = Object.objects.filter(classification=classification)
        serializer = ListSerializer(q, many=True)
        return Response(serializer.data)

class ClassificationView(APIView):
    def get(self, request):
        q = Classification.objects.all()
        serializer = ClassificationSerializer(q, many=True)
        return Response(serializer.data)

class DocumentView(APIView):
    parser_classes = (FileUploadParser)

    def get(self, request):
        queryset = Document.objects.order_by('-id')
        serializer = DocumentSerializer(queryset, many=True)
        return Response(serializer.data)