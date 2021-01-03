"""View module for handling requests about categorys"""
from django.http import HttpResponseServerError
from django.core.exceptions import ValidationError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from rest_framework.decorators import action
from neighborlyapi.models.category import Category

class Categories(ViewSet):
    """Categories"""

    def list(self, request):
        '''
        Handles GET requests to the /categories resource
        Method arguments:
            request -- The full HTTP request object
        URL: http://localhost:8000/categories
        Request Method: GET
        Response:
            list of all categories
        '''
        categories = Category.objects.all()

        serializer = CategorySerializer(
            categories, many=True, context={'request': request})

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

    def create(self, request):
        '''
        Handles POST requests to the /categories resource
        Method arguments:
            request -- The full HTTP request object
        URL: http://localhost:8000/categories
        Request Method: POST
        Payload:
        {
            "label": "example string"
        }
        Response:
            New Category Object
        '''
        category = Category()
        category.label = request.data["label"]

        try:
            category.save()
            serializer = CategorySerializer(
                category,
                context={'request': request}
            )
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        except ValidationError as ex:
            return Response(
                {"reason": ex.message},
                status=status.HTTP_400_BAD_REQUEST
            )

class CategorySerializer(serializers.ModelSerializer):
    """JSON serializer for categories
    Arguments:
        serializers
    """
    class Meta:
        model = Category
        fields = ('id', 'label')


