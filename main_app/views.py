from django.shortcuts import render
from .models import Chat
from .serializers import ChatSerializer
from django.http import HttpResponse
import pickle
import sklearn

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

model = pickle.load(open('model.sav', 'rb'))

# Create your views here.
@api_view(['GET', 'POST'])
def chat(request):

    if request.method == 'GET':
        return Response("hello, get")

    elif request.method == 'POST':
        print("this is thet data",request.data["message"])
        query = request.data["message"]
        model_input = [query]
        prediction = model.predict_proba(model_input)[0]
        proba_sad = prediction[0]
        proba_suicide = prediction[1]
        response = {"sad": proba_sad, "suicide": proba_suicide}
        return Response(response)
