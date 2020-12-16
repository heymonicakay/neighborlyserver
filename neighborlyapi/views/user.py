"""View module for handling requests about neighbors"""
from django.contrib.auth import get_user_model
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from rest_framework.decorators import action
from neighborlyapi.models.neighbor import Neighbor

class User(ViewSet):
    """Users"""

    def list(self, request):
        '''
        Handles GET requests to the /users resource
        Method arguments:
            request -- The full HTTP request object
        URL: http://localhost:8000/users
        Request Method: GET
        Response:
            list of all users
        '''
        neighbors = Neighbor.objects.all()

        serializer = NeighborSerializer(
            neighbors, many=True, context={'request': request})

        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """Handles GET requests to users resource for single User
        Written for User Profile View
        Returns:
            Response -- JSON serielized neighbor instance
        """
        try:
            neighbor = Neighbor.objects.get(pk=pk)

            neighbor.current_user = None
            current_user = Neighbor.objects.get(user=request.auth.user)

            if current_user.id == int(pk):
                neighbor.current_user = True
            else:
                neighbor.current_user = False

            serializer = NeighborSerializer(
                neighbor, many=False, context={'request': request})

            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )

        except Neighbor.DoesNotExist:
            return Response(
                {'message': 'User does not exist.'},
                status=status.HTTP_400_BAD_REQUEST
            )

class NeighborSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for neighbors
    Arguments:
        serializers
    """
    class Meta:
        model = Neighbor
        fields = ('id', 'bio', 'password', 'phone_number', 'username', 'admin',
        'active', 'first_name', 'last_name', 'full_name', 'email', 'joined_date')

