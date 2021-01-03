"""View module for handling requests about items"""
from django.http import HttpResponseServerError
from django.core.exceptions import ValidationError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import action
from neighborlyapi.models.item import Item
from neighborlyapi.models.neighbor import Neighbor
from neighborlyapi.models.category import Category
from neighborlyapi.models.itemtag import ItemTag
from neighborlyapi.models.condition import Condition
from neighborlyapi.views.category import CategorySerializer
from neighborlyapi.views.condition import ConditionSerializer
from neighborlyapi.views.itemtag import TagSerializer


class Items(ViewSet):
    """Items"""

    def list(self, request):
        '''
        Handles GET requests to the /items resource
        Method arguments:
            request -- The full HTTP request object
        URL: http://localhost:8000/items
        Request Method: GET
        Response:
            list of all items
        '''
        items = Item.objects.all()

        serializer = ItemSerializer(
            items, many=True, context={'request': request})

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

    def create(self, request):
        '''
        Handles Post requests to the /items resource
        Method arguments:
            request -- The full HTTP request object
        URL: http://localhost:8000/items
        Request Method: POST
        Payload: item object
            {
                "name": "Spade",
                "description": "It's a spade.",
                "listed_date": null,
                "brand": "The Grassroots",
                "serial_number": "451351658888",
                "category_id": 3,
                "condition_id": 2,
                "selected_tags": [
                    {
                        "id": 4,
                        "label": "muggles"
                    },
                    {
                        "id": 6,
                        "label": "firstyears"
                    },
                    {
                        "id": 8,
                        "label": "mandrake"
                    }
                ]
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
        owner = Neighbor.objects.get(user=request.auth.user)
        category = Category.objects.get(pk=request.data["category_id"])
        condition = Condition.objects.get(pk=request.data["condition_id"])

        item = Item()

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

class ItemSerializer(serializers.ModelSerializer):
    """JSON serializer for Items
    Arguments:
        serializers
    """
    category = CategorySerializer
    condition = ConditionSerializer
    class Meta:
        model = Item
        fields = ('id', 'owner', 'name', 'description', 'created_date', 'listed_date', 'brand', 'serial_number', 'category', 'condition', 'itemtags', 'active', 'draft', 'owner_full_name', 'owner_username' )
        depth = 1
