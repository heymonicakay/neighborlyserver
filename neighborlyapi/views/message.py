"""View module for handling requests about messages"""
from django.http import HttpResponseServerError
from django.core.exceptions import ValidationError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from rest_framework.decorators import action
from neighborlyapi.models.message import Message

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
                "reservation": 1,
                "recipient_id": 2,
                "read_date": null,
                "body": "THIS IS A MESSAGE BODY"
            }
            Response:
            {
                "id": 9,
                "owner": {
                    -owner object-
                },
                "name": "Spade",
                "description": "It's a spade.",
                "created_date": "2021-01-03",
                "listed_date": null,
                "brand": "The Grassroots",
                "serial_number": "451351658888",
                "category": {
                    "id": 3,
                    "label": "Technology"
                },
                "condition": {
                    "id": 2,
                    "label": "Seen Better Days"
                },
                "itemtags": [],
                "draft": true,
                "owner_full_name": "Harry Potter",
                "owner_username": "harrypotter"
            }
        '''
        sender = Neighbor.objects.get(user=request.auth.user)
        recipient = Neighbor.objects.get(pk=request.data["recipient_id"])

        item = Message()

        item.owner = owner
        item.category = category
        item.condition = condition

        item.name = request.data["name"]
        item.description = request.data["description"]
        item.selected_tags = request.data["selected_tags"]
        item.listed_date = request.data["listed_date"]
        item.brand = request.data["brand"]
        item.serial_number = request.data["serial_number"]

        # if request.data["item"] is not None:
        #     format, imgstr = request.data["post_img"].split(';base64,')
        #     ext = format.split('/')[-1]
        #     data = ContentFile(base64.b64decode(imgstr), name=f'"post_image"-{uuid.uuid4()}.{ext}')

        #     item.image_url = data

        try:
            item.save()
            serializer = ItemSerializer(item, context={'request': request})
            #iterate selected tags and save relationships to database
            for tag in item.selected_tags:

                itemtag = ItemTag()
                itemtag.tag_id = int(tag["id"])
                itemtag.item_id = int(serializer.data["id"])

                itemtag.save()

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)

class Message(serializers.HyperlinkedModelSerializer):
    """JSON serializer for messages
    Arguments:
        serializers
    """
    class Meta:
        model = Message
        fields = ('id', 'reservation', 'sender', 'recipient', 'status', 'sent_date', 'read_date', 'body')

