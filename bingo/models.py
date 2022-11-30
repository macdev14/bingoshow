from django.db import models

# Create your models here.
class Usuario(models.Model):
    nome = models.CharField(max_length=512)

    def __str__(self) -> str:
        return self.nome

class Resposta_incorreta(models.Model):
    enunciado = models.CharField(max_length=1000)

    class Meta:
        verbose_name = 'Resposta Incorreta'

    def __str__(self) -> str:
        return self.enunciado

class Resposta_correta(models.Model):
    enunciado = models.CharField(max_length=1000)
    
    class Meta:
        verbose_name = 'Resposta Correta'
    
    def __str__(self) -> str:
        return self.enunciado


class Categoria(models.Model):
    nome = models.CharField(max_length=512)

    def __str__(self) -> str:
        return self.nome

class Pergunta(models.Model):
    enunciado = models.CharField(max_length=1000, verbose_name='Pergunta')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    resposta_correta = models.ForeignKey(Resposta_correta, on_delete=models.CASCADE, verbose_name='Resposta Correta')
    resposta_incorreta = models.ManyToManyField(Resposta_incorreta, verbose_name='Resposta Incorreta')

    def __str__(self) -> str:
        return self.enunciado

class Tabela(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    # pergunta = models.ManyToManyField(Pergunta)
    pecas = models.CharField(max_length=25)





# class Tabela_usuario(models.Model):
#     # usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
#     # pergunta = models.ManyToManyField(Pergunta)
#     # pecas = models.CharField(max_length=24)
