"""
Auth View Set Module
Handles authentication and new user registration
"""
import json
import uuid
import base64
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.core.files.base import ContentFile
from rest_framework import status
from rest_framework.authtoken.models import Token
from neighborlyapi.models.neighbor import Neighbor

@csrf_exempt
def login_user(request):
    '''
    Handles authentication of an existing User
    Method arguments:
        request -- The full HTTP request object
    URL: http://localhost:8000/login
    Request Method: POST
    Body:
        {
            "username": "harrypotter",
            "password": "harry"
        }
    Response:
        {
        "valid": true,
        "token": "3ee1a4e07806f94208c787764843c2fa0cc3313b"
        }
    '''

    req_body = json.loads(request.body.decode())

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':

        username = req_body['username']
        password = req_body['password']
        authenticated_user = authenticate(username=username, password=password)

        # If authentication was successful, respond with True and the user's token
        if authenticated_user is not None:
            token = Token.objects.get(user=authenticated_user)
            data = json.dumps({"valid": True, "token": token.key})
            return HttpResponse(data, content_type='application/json')

        else:
            # if authentication fails, return False without a token
            data = json.dumps({"valid": False})
            return HttpResponse(data, content_type='application/json')

@csrf_exempt
def register_user(request):
    '''
    Handles the creation of a new user for authentication
    Method arguments:
        request -- The full HTTP request object
    URL: http://localhost:8000/register
    Request Method: POST
    Body:
        {
        "username": "harrypotter",
        "email": "harry@potter.com",
        "password": "harry",
        "first_name": "Harry",
        "last_name": "Potter",
        "bio": "Alohamora wand elf parchment, Wingardium Leviosa hippogriff, house dementors betrayal. Holly, Snape centaur portkey ghost Hermione spell bezoar Scabbers. Peruvian-Night-Powder werewolf, Dobby pear-tickle half-moon-glasses, Knight-Bus. Padfoot snargaluff seeker: Hagrid broomstick mischief managed. Snitch Fluffy rock-cake, 9 ¾ dress robes I must not tell lies. Mudbloods yew pumpkin juice phials Ravenclaw’s Diadem 10 galleons Thieves Downfall. Ministry-of-Magic mimubulus mimbletonia Pigwidgeon knut phoenix feather other minister Azkaban. Hedwig Daily Prophet treacle tart full-moon Ollivanders You-Know-Who cursed. Fawkes maze raw-steak Voldemort Goblin Wars snitch Forbidden forest grindylows wool socks.",
        "phone_number": "555-555-5555",
        "street_one": "4 Privet Drive",
        "street_two": "Under The Staircase",
        "city": "Surrey",
        "state": "TN",
        "zip": "37206"
        }
    Response:
        {
        "token": "3ee1a4e07806f94208c787764843c2fa0cc3313b"
        }
    '''

    # Load the JSON string of the request body into a dict
    req_body = json.loads(request.body.decode())

    # Create a new user by invoking the `create_user` helper method on Django's built-in User model
    new_user = User.objects.create_user(
        username=req_body['username'],
        email=req_body['email'],
        password=req_body['password'],
        first_name=req_body['first_name'],
        last_name=req_body['last_name'],
        is_active=True,
        is_staff=False
    )
    # format, imgstr = req_body["profile_image_url"].split(';base64,')
    # ext = format.split('/')[-1]
    # data = ContentFile(base64.b64decode(imgstr), name=f'{req_body["email"]}-{uuid.uuid4()}.{ext}')

    #neighbor has a property `user` which makes all `user` properties
    # accessible through the neighbor
    neighbor = Neighbor.objects.create(
        bio=req_body['bio'],
        user=new_user,
        phone_number=req_body['phone_number'],
        street_one=req_body['street_one'],
        street_two=req_body['street_two'],
        city=req_body['city'],
        state=req_body['state'],
        zip=req_body['zip']
    )

    # save it all to the db
    neighbor.save()

    # Use the REST Framework's token generator on the new user account
    token = Token.objects.create(user=new_user)

    # Return the token to the client
    data = json.dumps({"token": token.key})
    return HttpResponse(data, content_type='application/json', status=status.HTTP_201_CREATED)
