"""View module for handling requests about categorys"""
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from rest_framework.decorators import action
from neighborlyapi.models.category import Category

class Category(ViewSet):
    """Categorys"""

    def list(self, request):
        '''
        Handles GET requests to the /categorys resource
        Method arguments:
            request -- The full HTTP request object
        URL: http://localhost:8000/categorys
        Request Method: GET
        Response:
            list of all categorys
        '''
        categorys = Category.objects.all()

        serializer = CategorySerializer(
            categorys, many=True, context={'request': request})

        return Response(serializer.data)

class Category(serializers.HyperlinkedModelSerializer):
    """JSON serializer for categorys
    Arguments:
        serializers
    """
    class Meta:
        model = Category
        fields = ('id', 'label')

