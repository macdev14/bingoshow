import random
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from rest_framework import serializers, viewsets
from bingo.forms import UserForm
from .models import Tabela, Usuario, Pergunta, Categoria, Resposta_correta, Resposta_incorreta
from django.shortcuts import redirect
from random import randint
from django.urls import reverse
# Create your views here.
from django.template.defaulttags import register
from random import randint, choice
from django.db.models.aggregates import Count
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from rest_framework import filters
from django.http import HttpResponse
import json
@register.filter
def bingoletter():

    b = ['B', 'I', 'N', 'G', 'O']
    j = choice(b,k=1) + str(randint(1,75))
    print(j)
    return 1



class HomeView(TemplateView):
    template_name = 'bingo.html'

   
    def get_context_data(self, **kwargs):
        pk = self.kwargs["pk"]

        data = super().get_context_data(**kwargs)
        # data['tabela'] = self.request.session['0']
        # data['object'] = Tabela.objects.get(pk=pk)
        data['table'] = Tabela.objects.get(pk=pk).pecas.split()
        
        print(data['table'])
        return data

class UserView(CreateView):
    template_name = 'user.html'
    model = Usuario
    
    form_class = UserForm
  

    def get_success_url(self):
        # print(dir(self.request))
        t = Tabela.objects.create(usuario=self.object, pecas=self.gerar_numeros())
        # self.request.session['0'] = t
        return reverse('bingo:home',args=(t.pk,))

    def gerar_numeros(self):
        # print(dir(self.request))
        bingo = [randint(1, 75) for i in range(25)]
        # bingo[12]=0
        # self.request.session['0'] = bingo
        return ' '.join( str(i) for i in bingo)


class CategoriaSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Categoria
        fields = '__all__'

class RespostaIncorretaSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Resposta_incorreta
        fields = '__all__'

class RespostaCorretaSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Resposta_correta
        fields = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Usuario
        fields = '__all__'


# Serializers define the API representation.
class PerguntaSerializer(serializers.ModelSerializer):
    categoria = CategoriaSerializer(read_only=True)
    resposta_incorreta = RespostaIncorretaSerializer(read_only=True, many=True)
    resposta_correta = RespostaCorretaSerializer(read_only=True)
    class Meta:
        model = Pergunta
        fields = '__all__'

class TabelaSerializer(serializers.ModelSerializer):
    pergunta = PerguntaSerializer(read_only=True, many=True)
    usuario = UsuarioSerializer(read_only=True)
    class Meta:
        model = Tabela
        fields = '__all__'


# ViewSets define the view behavior.
class PerguntaViewSet(viewsets.ModelViewSet):
    
    serializer_class = PerguntaSerializer
    filter_backends = [filters.SearchFilter]
    
    def get_queryset(self):
        count = Pergunta.objects.aggregate(count=Count('id'))['count']
        random_index = randint(0, count - 1)
        j = Pergunta.objects.all()[random_index]
        return Pergunta.objects.filter(pk=j.id)




class TabelaViewSet(viewsets.ModelViewSet):
    
    serializer_class = TabelaSerializer
    
    filter_backends = [filters.SearchFilter]
    search_fields = ['usuario__id']
    def get_queryset(self):
        return Tabela.objects.all()       

class GerarTabela(APIView):
    bingo_letters = ['B', 'I', 'N', 'G', 'O']

    def gerar_numeros(self):
        # print(dir(self.request))
        bingo = []
        for i in range(25):
            # choice(self.bingo_letters) +
            b =  str(randint(1, 75))
            bingo.append(b)
        # bingo[14]='NONE'
        # self.request.session['0'] = bingo
        return ' '.join( str(i) for i in bingo)

    def post(self, request, format=None):
        userid = request.data.get('usuario')
        

        user = Usuario.objects.get(pk=userid)
        user_exists= Tabela.objects.filter(usuario=user).exists()
        print(user_exists)
        if user_exists:
            t = Tabela.objects.filter(usuario=user)[0]
        else: 
            t = Tabela.objects.create(usuario=user, pecas=self.gerar_numeros())
        return HttpResponse(json.dumps(t.pecas), content_type="application/json")

class UserViewSet(viewsets.ModelViewSet):
    
    serializer_class = UsuarioSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['id']
    def get_queryset(self):
        return Usuario.objects.all()      
 

    