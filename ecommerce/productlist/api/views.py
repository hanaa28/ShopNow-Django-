from rest_framework import views
from rest_framework.response import Response
from rest_framework.decorators import api_view
from productlist.models import *
from .serlizer import ProductsSerlizer

@api_view(['GET'])
def allProducts(request):
    data=Product.objects.all()
    datajson=ProductsSerlizer(data,many=True).data
    return Response({'data':datajson})




@api_view(['GET'])
def getProduct(request, id):
    details = ProductsSerlizer(Product.objects.get(id=id)).data
    return Response({'details': details})

@api_view(['GET'])
def getProductName(request,name):
    productName=ProductsSerlizer(Product.objects.get(name=name)).data
    return Response({'productName':productName})

@api_view(['POST'])
def addProduct(request):
    obj = ProductsSerlizer(data=request.data)
    if obj.is_valid():
        obj.save()
        return Response({'obj': 'Done'})
    else:
        return Response({'obj': 'wrong data', 'errors': obj.errors})
@api_view(['PUT'])
def updateProduct(request, id):
    updateObject = Product.objects.filter(id=id).first()
    if updateObject:
        serializer = ProductsSerlizer(instance=updateObject, data=request.data)
        if serializer.is_valid():
            serializer.save()  
            return Response(serializer.data)
        else:
            return Response(serializer.errors) 
    else:
        return Response({'msg': 'Product is Not Found'})


@api_view(['DELETE'])
def deleteProduct(request, id): 
    prod=Product.objects.filter(id=id)
    if(len(prod)>0):
     prod.delete()
    return Response({'msg': 'Product is Deleted'})