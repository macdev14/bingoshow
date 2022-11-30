from django.contrib import admin
from bingo.models import *
from django.core.exceptions import ValidationError
from django import forms
# Register your models here.
admin.site.register(Categoria)
admin.site.register(Tabela)
admin.site.register(Usuario)
admin.site.register(Resposta_correta)
admin.site.register(Resposta_incorreta)


class QuestionForm(forms.ModelForm):
    model = Pergunta

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get('resposta_incorreta').count() != 3:
            raise ValidationError('Você deve escolher exatamente 3 respostas incorretas para o campo Outras respostas!')

@admin.register(Pergunta)
class QuestionAdmin(admin.ModelAdmin):
    form = QuestionForm