from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ProductSerializers
from .models import Product


@api_view(['GET'])
def ShowAll(request):
    products = Product.objects.all()
    serializer = ProductSerializers(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def ViewProduct(request,pk):
    product=Product.objects.get(id=pk)
    serializer = ProductSerializers(product, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def CreateProduct(request):
    product=request.data
    serializer = ProductSerializers(product)
    if serializer.is_valid():
        serializer.save()


    return Response(serializer.data)

@api_view(['POST'])
def UpdateProduct(request,pk):
    product=Product.objects.get(id=pk)
    serializer = ProductSerializers(instance=product, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['GET'])
def DeleteProduct(request,pk):
    product=Product.objects.get(id=pk)
    product.delete()

    return Response('item deleted successfully')

