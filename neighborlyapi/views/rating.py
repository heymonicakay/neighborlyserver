"""View module for handling requests about ratings"""
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from rest_framework.decorators import action
from neighborlyapi.models.rating import Rating

class Rating(ViewSet):
    """Ratings"""

    def list(self, request):
        '''
        Handles GET requests to the /ratings resource
        Method arguments:
            request -- The full HTTP request object
        URL: http://localhost:8000/ratings
        Request Method: GET
        Response:
            list of all ratings
        '''
        ratings = Rating.objects.all()

        serializer = RatingSerializer(
            ratings, many=True, context={'request': request})

        return Response(serializer.data)

class Rating(serializers.HyperlinkedModelSerializer):
    """JSON serializer for ratings
    Arguments:
        serializers
    """
    class Meta:
        model = Rating
        fields = ('id', 'label')

