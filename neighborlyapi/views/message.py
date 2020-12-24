"""View module for handling requests about messages"""
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from rest_framework.decorators import action
from neighborlyapi.models.message import Message

class Message(ViewSet):
    """Messages"""

    def list(self, request):
        '''
        Handles GET requests to the /messages resource
        Method arguments:
            request -- The full HTTP request object
        URL: http://localhost:8000/messages
        Request Method: GET
        Response:
            list of all messages
        '''
        messages = Message.objects.all()

        serializer = MessageSerializer(
            messages, many=True, context={'request': request})

        return Response(serializer.data)

class Message(serializers.HyperlinkedModelSerializer):
    """JSON serializer for messages
    Arguments:
        serializers
    """
    class Meta:
        model = Message
        fields = ('id', 'body')

