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
    risk = 0
    level1 = 0
    level2 = 25
    level3 = 50
    level4 = 75
    level5 = 100

    if request.method == 'GET':
        return Response("hello, get")

    elif request.method == 'POST':
        print("this is thet data",request.data["message"])
        query = request.data["message"]
        model_input = [query]
        prediction = model.predict_proba(model_input)[0]
        proba_suicide = round(prediction[1]*100)

        if proba_suicide > level1 and proba_suicide <= level2:
            risk = 1
        if proba_suicide > level2 and proba_suicide <= level3:
            risk = 2
        if proba_suicide > level3 and proba_suicide <= level4:
            risk = 3
        if proba_suicide > level4 and proba_suicide <= level5:
            risk = 4
        response = {"risk": risk}
        return Response(response)
