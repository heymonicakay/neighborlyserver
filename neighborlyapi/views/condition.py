"""View module for handling requests about conditions"""
from django.http import HttpResponseServerError
from django.core.exceptions import ValidationError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from rest_framework.decorators import action
from neighborlyapi.models.condition import Condition

class Conditions(ViewSet):
    """Conditions"""

    def list(self, request):
        '''
        Handles GET requests to the /conditions resource
        Method arguments:
            request -- The full HTTP request object
        URL: http://localhost:8000/conditions
        Request Method: GET
        Response:
            list of all conditions
        '''
        conditions = Condition.objects.all()

        serializer = ConditionSerializer(
            conditions, many=True, context={'request': request})

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

class ConditionSerializer(serializers.ModelSerializer):
    """JSON serializer for conditions
    Arguments:
        serializers
    """
    class Meta:
        model = Condition
        fields = ('id', 'label')
