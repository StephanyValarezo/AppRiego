from rest_framework import serializers

from webAppW.models import Sensores
from rest_basic.models import Article, Valvulas_Water

class SensoresSerializer(serializers.ModelSerializer):

    class Meta:
        model=Sensores
        fields=['id','nombre','mensaje']
        

class ArticleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Article
        #fields =['id','title','author','email']
        fields='__all__'


class ValvulasSerializers(serializers.ModelSerializer):
    class Meta:
        model = Valvulas_Water
        fields='__all__'