"""View module for handling requests about descriptionaccuracys"""
from django.http import HttpResponseServerError
from django.core.exceptions import ValidationError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from rest_framework.decorators import action
from neighborlyapi.models.descriptionaccuracy import DescriptionAccuracy

class DescriptionAccuracys(ViewSet):
    """DescriptionAccuracys"""

    def list(self, request):
        '''
        Handles GET requests to the /descriptionaccuracys resource
        Method arguments:
            request -- The full HTTP request object
        URL: http://localhost:8000/descriptionaccuracys
        Request Method: GET
        Response:
            list of all descriptionaccuracys
        '''
        descriptionaccuracys = DescriptionAccuracy.objects.all() 

        serializer = DescriptionAccuracySerializer(
            descriptionaccuracys, many=True, context={'request': request})

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

class DescriptionAccuracySerializer(serializers.ModelSerializer):
    """JSON serializer for descriptionaccuracys
    Arguments:
        serializers
    """
    class Meta:
        model = DescriptionAccuracy
        fields = ('id', 'label')
