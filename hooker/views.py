from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import HookerSerializer


class HookerAPI(APIView):
    """
    Prints out a post response
    """

    def post(self, request, format=None):
        serializer = HookerSerializer(data=request.data)
        if serializer.is_valid():
            #serializer.save()
            return Response(
                        serializer.data,
                        status=status.HTTP_201_CREATED)
        return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST)

