from django.shortcuts import render
from rest_framework.decorators import action, api_view
from .serializes import *
from rest_framework import viewsets
from rest_framework.decorators import authentication_classes , permission_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


@api_view(['POST'])
def HomeView(request):
    img = request.FILES['img']
    text = request.POST.get('text')
    rasm = Home.objects.create(img=img,  text=text)
    ser = HomeSerializer(rasm)
    return Response(ser.data)




@api_view(['POST'])
def AboutView(request):
    img = request.FILES['img']
    text = request.POST.get('text')
    rasm = Home.objects.create(img=img,  text=text)
    ser = HomeSerializer(rasm)
    return Response(ser.data)



class HomeViews(viewsets.ModelViewSet):
    queryset = Home.objects.all()
    serializer_class =HomeSerializer
























