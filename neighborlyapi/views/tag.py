"""View module for handling requests about tags"""
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from rest_framework.decorators import action
from neighborlyapi.models.tag import Tag

class Tag(ViewSet):
    """Tags"""

    def list(self, request):
        '''
        Handles GET requests to the /tags resource
        Method arguments:
            request -- The full HTTP request object
        URL: http://localhost:8000/tags
        Request Method: GET
        Response:
            list of all tags
        '''
        tags = Tag.objects.all()

        serializer = TagSerializer(
            tags, many=True, context={'request': request})

        return Response(serializer.data)

class Tag(serializers.HyperlinkedModelSerializer):
    """JSON serializer for tags
    Arguments:
        serializers
    """
    class Meta:
        model = Tag
        fields = ('id', 'label')

