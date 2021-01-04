"""View module for handling requests about messages"""
from django.http import HttpResponseServerError
from django.core.exceptions import ValidationError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import action
from ..models.message import Message
from ..models.neighbor import Neighbor
from ..models.reservation import Reservation


class Messages(ViewSet):
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

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

    def create(self, request):
        '''
        Handles Post requests to the /messages resource
        Method arguments:
            request -- The full HTTP request object
        URL: http://localhost:8000/messages
        Request Method: POST
        Payload: message object
            {
                "reservation_id": 1,
                "recipient_id": 2,
                "read_date": null,
                "body": "THIS IS A MESSAGE BODY"
            }
            Response:
            {
            }
        '''
        sender = Neighbor.objects.get(user=request.auth.user)
        recipient = Neighbor.objects.get(pk=request.data["recipient_id"])
        reservation = Reservation.objects.get(pk=request.data["reservation_id"])

        message = Message()

        message.reservation = reservation
        message.sender = sender
        message.recipient = recipient

        message.body = request.data["body"]

        try:
            message.save()
            serializer = MessageSerializer(message, context={'request': request})

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)

class MessageSerializer(serializers.ModelSerializer):
    """JSON serializer for messages
    Arguments:
        serializers
    """
    class Meta:
        model = Message
        fields = ('id', 'reservation', 'sender', 'recipient', 'sent_date', 'read_date', 'body', 'read')

