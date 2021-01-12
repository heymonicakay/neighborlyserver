"""View module for handling requests about neighbors"""
from django.contrib.auth import get_user_model
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from rest_framework.decorators import action
from neighborlyapi.models.neighbor import Neighbor

class Users(ViewSet):
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
        URL: http://localhost:8000/users/1
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
    @action(methods=['get'], detail=False)
    def current_user(self, request):
        """docstrings"""
        current_user = Neighbor.objects.get(user=request.auth.user)

        serializer = NeighborSerializer(
            current_user, context={'request': request})

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

class UserSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for Users

    Arguments:
        serializers
    """
    class Meta:
        model = get_user_model()
        fields = ('id', 'url', 'username', 'password', 'first_name', 'last_name', 'email', 'is_active', 'date_joined', 'is_staff')

class NeighborSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for neighbors
    Arguments:
        serializers
    """
    user = UserSerializer(many=False)
    class Meta:
        model = Neighbor
        fields = ('id', 'bio', 'user', 'phone_number', 'full_name', 'city', 'state', 'zip', 'images' )

