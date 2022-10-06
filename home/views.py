from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from home.models import Coin_Market
from home.serializers import CoinMarketSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

@csrf_exempt
@api_view(['GET', 'POST', 'PUT'])
def cryptocurrency(request):
    if request.method == 'GET':
        coin_market     = Coin_Market.objects.all()
        serializer      = CoinMarketSerializer(coin_market, many=True)
        return Response({'success':True, 'data':serializer.data, "status": 200}, status=status.HTTP_200_OK)

    elif request.method == 'POST':

        serializer = CoinMarketSerializer(data=request.data)
        if serializer.is_valid():
            serializer.create(validated_data=request.data)

        return Response({'success':True, "status":200}, status=status.HTTP_200_OK)

    elif request.method == 'PUT':

        serializer = CoinMarketSerializer(data=request.data)
        if serializer.is_valid():
            serializer.update(validated_data=request.data)

        return Response({'success':True, "status":200}, status=status.HTTP_200_OK)