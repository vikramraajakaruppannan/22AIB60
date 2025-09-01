from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import URL
from .serializers import URLSerializer
import random
import string

def generate_shortcode(length=6):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

@api_view(['POST'])
def create_short_url(request):
    serializer = URLSerializer(data=request.data, context={'request': request})
    if serializer.is_valid():
        url_obj = serializer.save()
        response_serializer = URLSerializer(url_obj, context={'request': request})
        return Response({
            "shortLink": response_serializer.data["shortLink"],
            "expiry": response_serializer.data["expiry"]
        }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def redirect_to_url(request, shortcode):
    try:
        url = URL.objects.get(shortcode=shortcode)
        return Response({'original_url': url.original_url}, status=status.HTTP_302_FOUND)
    except URL.DoesNotExist:
        return Response({'error': 'URL not found'}, status=status.HTTP_404_NOT_FOUND)
    
