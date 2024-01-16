from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(["GET"])
def register_page(request):
    return Response ({"message":"Hi i am from the backend"})