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


class ReservationSerializer(serializers.ModelSerializer):
    """JSON serializer for reservations
    Arguments:
        serializers
    """
    class Meta:
        model = Reservation
        fields = ('id', 'item', 'user', 'requested_start', 'messages', 'requested_end', 'start', 'end', 'res_status')
        depth = 1
