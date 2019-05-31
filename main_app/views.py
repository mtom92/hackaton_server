from django.shortcuts import render
from .models import Chat
from .serializers import ChatSerializer
from django.http import HttpResponse
import joblib


from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['GET', 'POST'])
def chat(request):
    if request.method == 'GET':
        the_model = joblib.load('filename.pkl')
        response = the_model.grapher("Very stress")
        return Response(response)
    elif request.method == 'POST':
        return Response("hello, post")
