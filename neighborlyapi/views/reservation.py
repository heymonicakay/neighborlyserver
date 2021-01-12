"""View module for handling requests about messages"""
from django.http import HttpResponseServerError
from django.core.exceptions import ValidationError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import action
from ..models.reservation import Reservation
from ..models.reservation_status import ReservationStatus
from ..models.neighbor import Neighbor
from ..models.item import Item

class Reservations(ViewSet):
    """Reservations"""

    def list(self, request):
        '''
        Handles GET requests to the /reservations resource
        Method arguments:
            request -- The full HTTP request object
        URL: http://localhost:8000/reservations
        Request Method: GET
        Response:
            list of all reservations
        '''
        reservations = Reservation.objects.all()

        serializer = ReservationSerializer(
            reservations, many=True, context={'request': request})

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

    @action(methods=['patch'], detail=True)
    def manage(self, request, pk=None):
        """Manages users approving reservation requests"""
            # http://localhost:8000/reservations/1/manage?status=2

        res = Reservation.objects.get(pk=pk)

        res_status = ReservationStatus.objects.get(pk=self.request.query_params.get('status', None))

        res.res_status = res_status
        res.save()

        serializer = ReservationSerializer(res, context={'request': request})
        return Response(serializer.data)

    def create(self, request):
        '''
        Handles Post requests to the /reservations resource
        Method arguments:
            request -- The full HTTP request object
        URL: http://localhost:8000/messages
        Request Method: POST
        Payload: message object
            {
                "item_id": ,
                "requested_start": "2020-01-30"
                "requested_end": "2020-02-02"
            }
            Response:
            {
            }
        '''
        current_user = Neighbor.objects.get(user=request.auth.user)
        item = Item.objects.get(pk=request.data["item_id"])
        start = request.data['requested_start']
        end = request.data['requested_end']

        reservation = Reservation()


        reservation.user = current_user
        reservation.item = item
        reservation.res_status = 1
        reservation.requested_start = start
        reservation.requested_end = end

        try:
            reservation.save()
            serializer = ReservationSerializer(reservation, context={'request': request})

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)

class ReservationSerializer(serializers.ModelSerializer):
    """JSON serializer for reservations
    Arguments:
        serializers
    """
    class Meta:
        model = Reservation
        fields = ('id', 'item', 'user', 'requested_start', 'messages', 'requested_end', 'start', 'end', 'res_status')
        depth = 3
