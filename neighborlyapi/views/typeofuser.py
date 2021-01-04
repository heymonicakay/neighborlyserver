"""View module for handling requests about types of users"""
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from rest_framework.decorators import action
from neighborlyapi.models.type_of_user import TypeOfUser

class TypesOfUsers(ViewSet):
    """TypesOfUsers"""

    def list(self, request):
        '''
        Handles GET requests to the /typesofusers resource
        Method arguments:
            request -- The full HTTP request object
        URL: http://localhost:8000/typesofusers
        Request Method: GET
        Response:
            list of all types of users
        '''
        types = TypeOfUser.objects.all()

        serializer = TypeOfUserSerializer(
            types, many=True, context={'request': request})

        return Response(serializer.data)

class TypeOfUserSerializer(serializers.ModelSerializer):
    """JSON serializer for ratings
    Arguments:
        serializers
    """
    class Meta:
        model = TypeOfUser
        fields = ('id', 'label')
