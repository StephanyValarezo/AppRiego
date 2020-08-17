from django.shortcuts import render
from django.http import HttpRequest, JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser
from rest_basic.models import Article, Valvulas_Water
from rest_basic.serializers import ArticleSerializers, ValvulasSerializers
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from rest_framework import generics
from rest_framework import mixins

# Create your views here.

class GenericAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin,mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    serializer_class = ValvulasSerializers
    queryset = Valvulas_Water.objects.all()

    lookup_field = 'id'

    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

        return self.list(request)
    
    def post (self, request):
        return self.create(request)
    
    def put(self, request, id=None):
        return self.update(request, id)

    def delete(self, request, id):
        return self.destroy(request, id)
        








class ValvulasAPIView(APIView):

    def get(self, request):
        articles = Valvulas_Water.objects.all()
        serializer = ValvulasSerializers(articles, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ValvulasSerializers(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ArticleDetails(APIView):

    def get_object(self, id):
        try: 
            return Valvulas_Water.objects.get(id=id)

        except Valvulas_Water.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    
    def get(self, request, id):
        article= self.get_object(id)
        serializer = ValvulasSerializers(article)
        return Response(serializer.data)
        
    def put(self, request, id):
        article= self.get_object(id)
        serializer = ValvulasSerializers(article,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        article= self.get_object(id)
        article.delete()
    
        return Response(status=status.HTTP_204_NO_CONTENT)

    



#@csrf_exempt
@api_view(['GET','POST'])
def article_list(request):

    if request.method =='GET':
        articles = Valvulas_Water.objects.all()
        serializer = ValvulasSerializers(articles, many=True)
        #return JsonResponse(serializer.data, safe=False)
        return Response(serializer.data)

    elif request.method == 'POST':
        #data= JSONParser().parse(request)
        serializer = ValvulasSerializers(data=request.data)

        if serializer.is_valid():
            serializer.save()
            #return JsonResponse(serializer.data, status=201)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        #return JsonResponse(serializer.errors, status=400)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#@csrf_exempt
@api_view(['GET','PUT','DELETE'])
def article_detail(request, pk):
    try:
        article = Valvulas_Water.objects.get(pk=pk)

    except Valvulas_Water.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ValvulasSerializers(article)
        return Response(serializer.data)
    
    elif request.method =='PUT':
        #data= JSONParser().parse(request)
        serializer = ValvulasSerializers(article,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        article.delete()
        #return HttpResponse(status=204)
        return Response(status=status.HTTP_204_NO_CONTENT)

    


