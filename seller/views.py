from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import Product
from . serializers import ProductSerializer

class Productlist(APIView):

    def get(self,request):
        Product1 =Product.objects.all()
        serializer=ProductSerializer(Product,many=true)
        return Response (serializer.data)

    def post(self):
        pass
