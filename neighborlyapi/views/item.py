"""View module for handling requests about items"""
from django.http import HttpResponseServerError
from django.core.exceptions import ValidationError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import action
from neighborlyapi.views.category import CategorySerializer
from neighborlyapi.views.condition import ConditionSerializer
from neighborlyapi.views.reservation import ReservationSerializer
from ..models.item import Item
from ..models.neighbor import Neighbor
from ..models.category import Category
from ..models.item_tag import ItemTag
from ..models.item_review import ItemReview
from ..models.condition import Condition
from ..models.reservation_status import ReservationStatus
from ..models.reservation import Reservation
from ..models.description_accuracy import DescriptionAccuracy

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
        current_user = Neighbor.objects.get(user=request.auth.user)

        owner_id = self.request.query_params.get('owner_id', None)
        category_id = self.request.query_params.get('category_id', None)

        if owner_id is not None:
            # http://localhost:8000/items?owner_id=10
            owner = Neighbor.objects.get(pk=owner_id)

            items_by_owner = items.filter(
                owner=owner)

            serializer = ItemSerializer(
                items_by_owner, many=True, context={'request': request}
            )
            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )

        elif category_id is not None:
            # http://localhost:8000/items?category_id=2
            category = Category.objects.get(pk=category_id)
            posts = posts.filter(
                category=category)

        serializer = ItemSerializer(
            items, many=True, context={'request': request})

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

    def retrieve(self, request, pk=None):
        """Handle GET request for single item
        Returns:
            Response JSON serielized item instance
        """
        try:
            item = Item.objects.get(pk=pk)

            serializer = ItemSerializer(
                item, context={'request': request})
            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )
        except Exception as ex:
            return HttpResponseServerError(ex)

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


    @action(methods=['post'], detail=True)
    def reserve(self, request, pk=None):
        '''
        Handles Post requests to the /reservations resource
        Method arguments:
            request -- The full HTTP request object
        URL: http://localhost:8000/items/1/reserve
        Request Method: POST
        Payload: reservation object
            {
                "requested_start": "2021-01-15",
                "requested_end": "2021-01-16",
                "start": null,
                "end": null
            }
            Response:
            {
            }
        '''
        user = Neighbor.objects.get(user=request.auth.user)
        item = Item.objects.get(pk=pk)
        res_status = ReservationStatus.objects.get(pk=1)

        reservation = Reservation()

        reservation.user = user
        reservation.item = item
        reservation.res_status = res_status
        reservation.requested_start = request.data["requested_start"]
        reservation.requested_end = request.data["requested_end"]
        reservation.start = request.data["start"]
        reservation.end = request.data["end"]

        try:
            reservation.save()
            serializer = ReservationSerializer(reservation, context={'request': request})

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)


    @action(methods=['post'], detail=True)
    def review(self, request, pk=None):
        '''
        Handles Post requests to the /items resource
        Method arguments:
            request -- The full HTTP request object
        URL: http://localhost:8000/items/3/review
        Request Method: POST
        Payload: review object
            {
                "reservation_id": 1,
                "rating": 5,
                "description_accuracy_id": 2,
                "details": "It was on the corner of the street that he noticed the first sign of something peculiar -- a cat reading a map. For a second, Mr. Dursley didn't realize what he had seen -- then he jerked his head around to look again.",
                "subject": "Portkey"
            }
            Response:
            {
            }
        '''
        reviewer = Neighbor.objects.get(user=request.auth.user)
        item = Item.objects.get(pk=pk)
        reservation = Reservation.objects.get(pk=request.data["reservation_id"])
        desc_acc = DescriptionAccuracy.objects.get(pk=request.data["description_accuracy_id"])

        item_review = ItemReview()

        item_review.reservation = reservation
        reservation.item = item
        item_review.reviewer = reviewer
        item_review.rating = request.data["rating"]
        item_review.description_accuracy = desc_acc
        item_review.details = request.data["details"]
        item_review.subject = request.data["subject"]

        try:
            item_review.save()
            serializer = ItemReviewSerializer(item_review, context={'request': request})

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)

class ItemReviewSerializer(serializers.ModelSerializer):
    """JSON serializer for Items
    Arguments:
        serializers
    """
    class Meta:
        model = ItemReview
        fields = ('id', 'reservation', 'reviewer', 'description_accuracy', 'created_date', 'details', 'subject',)
        depth = 1

class ItemSerializer(serializers.ModelSerializer):
    """JSON serializer for Items
    Arguments:
        serializers
    """
    category = CategorySerializer
    condition = ConditionSerializer
    class Meta:
        model = Item
        fields = ('id', 'owner', 'name', 'description', 'created_date', 'listed_date', 'brand', 'serial_number', 'reservations', 'category', 'condition', 'itemtags', 'itemimages', 'active', 'draft', 'owner_full_name', 'owner_username', 'item_reviews' )
        depth = 1
