from .serializer import PlayerSerializer, NewsSerializer,  FormerPlayerSerializer, GallerySerializer, StaffSerializer, ShopSerializer,SponserSerializer
from core.models import Player, FormerPlayer, News, Gallery, Staff, Shop,Sponser
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from django.http import JsonResponse


class PlayerList(generics.ListAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

class NewsList(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

class SponserList(generics.ListAPIView):
    queryset = Sponser.objects.all()
    serializer_class = SponserSerializer

class FormerPlayerList(generics.ListAPIView):
    queryset = FormerPlayer.objects.all()
    serializer_class = FormerPlayerSerializer

class GalleryList(generics.ListAPIView):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer


class StaffList(generics.ListAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer

class ShopList(generics.ListAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer


class PlayerView(APIView):
    def get(self, request):
        players = Player.objects.all()
        serializer = PlayerSerializer(players, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PlayerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Player created successfully'}, status=201)
        return Response(serializer.errors, status=400)


class StaffDetail(APIView):
    def get(self, request, id):
        staff = get_object_or_404(Staff, id=id)
        serializer = StaffSerializer(staff)
        data = serializer.data
        data['src'] = request.build_absolute_uri(data['src'])
        return Response(data)
    
from django.urls import reverse
from rest_framework.response import Response
from rest_framework.views import APIView


class PlayerDetail(APIView):
    def get(self, request, slug):
        staff = get_object_or_404(Player, slug=slug)
        serializer = PlayerSerializer(staff)
        data = serializer.data
        data['src'] = request.build_absolute_uri(data['src'])
        return Response(data)