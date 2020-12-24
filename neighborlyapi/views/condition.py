"""View module for handling requests about conditions"""
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from rest_framework.decorators import action
from neighborlyapi.models.condition import Condition

class Condition(ViewSet):
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

        return Response(serializer.data)

class Condition(serializers.HyperlinkedModelSerializer):
    """JSON serializer for conditions
    Arguments:
        serializers
    """
    class Meta:
        model = Condition
        fields = ('id', 'label')

