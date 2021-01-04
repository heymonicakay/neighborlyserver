"""View module for handling requests about itemtags"""
from django.http import HttpResponseServerError
from django.core.exceptions import ValidationError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from neighborlyapi.models.item_tag import ItemTag
from neighborlyapi.models.tag import Tag
from neighborlyapi.models.item import Item

class ItemTags(ViewSet):
    """Item Tags"""

    def list(self, request):
        '''
        Handles GET requests to the /itemtags resource
        Method arguments:
            request -- The full HTTP request object
        URL: http://localhost:8000/itemtags
        Request Method: GET
        Response:
            list of all messages

        URL: http://localhost:8000/itemtags?item=2
        Request Method: GET
        Response:
            list of all itemtags
        '''
        itemtags = ItemTag.objects.all()
        #filtering itemtags by item
        item_id = self.request.query_params.get("item_id", None)
        if item_id is not None:
            itemtags = itemtags.filter(item_id=item_id)

        serializer = ItemTagSerializer(
            itemtags, many=True, context={'request': request})
        return Response(serializer.data)

    def create(self, request):
        '''
        Handles POST requests to the /itemtags resource
        Method arguments:
            request -- The full HTTP request object
        URL: http://localhost:8000/itemtags
        Request Method: POST
        Payload:
            {
                "item_id": 1,
                "tag_id": 1
            }
        Response:
            {
            "id": 6,
            "item_id": 1,
            "tag": {
                "id": 1,
                "label": "toad"
                }
            }
        '''
        item = Item.objects.get(pk=request.data["item_id"])
        tag = Tag.objects.get(pk=request.data["tag_id"])

        itemtag = ItemTag()
        itemtag.item = item
        itemtag.tag = tag

        try:
            ItemTag.objects.get(item=item, tag=tag)
            return Response(
                {'message': ' This ItemTag Already Exists.'},
                status=status.HTTP_422_UNPROCESSABLE_ENTITY
            )

        except ItemTag.DoesNotExist:
            itemtag.save()
            serializer = ItemTagSerializer(itemtag, context={'request': request})
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

    def destroy(self, request, pk=None):
        """Handles DELETE requests to the /itemtags resource
        Method arguments:
            request -- The full HTTP request object
        URL: http://localhost:8000/itemtags/6
        Request Method: DELETE
        RESPONE: 204  NO CONTENT
        """
        try:
            itemtag = ItemTag.objects.get(pk=pk)
            itemtag.delete()

            return Response(
                {},
                status=status.HTTP_204_NO_CONTENT
            )

        except ItemTag.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response(
                {'message': ex.args[0]},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

class TagSerializer(serializers.ModelSerializer):
    """JSON serializer for tags"""
    class Meta:
        model = Tag
        fields = ('id', 'label')


class ItemTagSerializer(serializers.ModelSerializer):
    """JSON serializer for itemtags"""

    tag = TagSerializer(many=False)
    class Meta:
        model = ItemTag
        fields = ('id', 'tag',)
