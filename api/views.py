from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.http import QueryDict

from .models import Inventory
from .serializers import InventorySerializer


@api_view(['GET','POST'])
def alldata(request):
    if request.method == "GET":
        inventories = Inventory.objects.all()
        serializer = InventorySerializer(inventories, many=True)
        return Response(serializer.data)
    
    if request.method=="POST":
        serializer=InventorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


   

@api_view(['GET','PUT','DELETE'])
def singledata(req,id):
    try:
        inventory=Inventory.objects.get(id=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if req.method=="GET":
        serializer=InventorySerializer(inventory)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    elif req.method=="PUT":
        # req_data=QueryDict(req.body.decode('utf-8'))
        serializer=InventorySerializer(inventory,data=req.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif req.method=="DELETE":
        inventory.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(["GET"])
def browse_cat(req,cat):
    try:
       catbooks=Inventory.objects.filter(category=cat)
    except:
       return Response({},status=status.HTTP_404_NOT_FOUND)
   
    if req.method=="GET":
       serializer=InventorySerializer(catbooks,many=True)
       return Response(serializer.data)
    else:
        return Response({},status=status.HTTP_400_BAD_REQUEST)