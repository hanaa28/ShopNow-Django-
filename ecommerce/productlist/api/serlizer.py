from rest_framework import serializers
from productlist.models import *


class ProductsSerlizer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'add_date', 'image']


# class ProductsSerlizer(serializers.Serializer):
#     id=serializers.IntegerField(read_only=True)
#     name=serializers.CharField(max_length=100)
#     price=serializers.IntegerField()
#     createdate=serializers.DateTimeField(read_only=True)
#     image=serializers.ImageField()



def create(self, validated_data):
        return Product.objects.create(validated_data)  

def update(self,instance, validated_data):
      instance.name=validated_data.get('name')
      instance.price=validated_data.get('price')
      instance.image=validated_data.get('image')
      instance.save()
      return instance