"""docstrings"""
# https://www.base64-image.de/ for image encoding and postman tests

import uuid
import base64
from django.http.response import HttpResponseServerError
from django.core.exceptions import ValidationError
from django.core.files.base import ContentFile
from django.utils import timezone
from rest_framework.viewsets import ViewSet
from rest_framework import serializers, status
from rest_framework.decorators import action
from rest_framework.response import Response
from ..models.item_image import ItemImage
from ..models.item import Item

class ItemImages(ViewSet):
    """docstrings"""

    def create(self, request):
        """docstrings"""
        item_image = ItemImage()

        format, imgstr = request.data["image"].split(';base64,')
        ext = format.split('/')[-1]
        data = ContentFile(base64.b64decode(imgstr), name=f'"image"-{uuid.uuid4()}.{ext}')

        item_image.image = data

        item_image.save()
        serializer = ItemImageSerializer(item_image, context={'request': request})

        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )


    def list(self, request):
        """Handles GET request for item images"""
        images = ItemImage.objects.all()

        serializer = ItemImageSerializer(
            images, many=True, context={'request': request}
        )
        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

    def retrieve(self, request, pk=None):
        """Handle PUT requests for posts"""
        try:
            item_image = ItemImage.objects.get(pk=pk)

            serializer = ItemImageSerializer(
                item_image, context={'request': request})

            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )

        except Exception as ex:
            return HttpResponseServerError(ex)

    @action(methods=['patch'], detail=True)
    def savetoitem(self, request, pk=None):
        """Manages admins approving posts"""

        item = Item.objects.get(pk=request.data["item"])
        item_image = ItemImage.objects.get(pk=pk)

        item_image.item = item

        item_image.save()

        serializer = ItemImageSerializer(
            item_image, context={'request': request}
        )

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

    def destroy(self, request, pk=None):
        """Handle DELETE requests for a single post
        Returns:
            Response -- 200, 404, or 500 status code
        """
        try:
            item_image = ItemImage.objects.get(pk=pk)
            item_image.delete()

            return Response(
                {},
                status=status.HTTP_204_NO_CONTENT
            )

        except ItemImage.DoesNotExist as ex:
            return Response(
                {'message': ex.args[0]},
                status=status.HTTP_404_NOT_FOUND
            )

        except Exception as ex:
            return Response(
                {'message': ex.args[0]},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

class ItemImageSerializer(serializers.ModelSerializer):
    """Serializer for ItemImage """
    class Meta:
        model = ItemImage
        fields = ('id', 'image', 'item')
