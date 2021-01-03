"""View module for handling requests about tags"""
from django.http import HttpResponseServerError
from django.core.exceptions import ValidationError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from rest_framework.decorators import action
from neighborlyapi.models.tag import Tag

class Tags(ViewSet):
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

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

    def create(self, request):
        '''
        Handles POST requests to the /tags resource
        Method arguments:
            request -- The full HTTP request object
        URL: http://localhost:8000/tags
        Request Method: POST
        Payload:
        {
            "label": "example string"
        }
        Response:
            New Category Object
        '''
        tag = Tag()
        tag.label = request.data["label"]

        try:
            tag.save()
            serializer = TagSerializer(
                tag,
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

class TagSerializer(serializers.ModelSerializer):
    """JSON serializer for tags
    Arguments:
        serializers
    """
    class Meta:
        model = Tag
        fields = ('id', 'label')

