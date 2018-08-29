from rest_framework import serializers
from home.models import *


class producto_serializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Producto 
        fields = ('url','id','nombre','precio','foto','status','stock','marca','categorias',)

class marca_serializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Marca 
        fields =('url','id','nombre',)

class categoria_serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Categoria 
        fields = ('url','nombre',)     