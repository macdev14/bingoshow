# Generated by Django 4.1.3 on 2022-11-23 11:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bingo', '0002_pergunta_enunciado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tabela',
            name='pergunta',
        ),
        migrations.AlterField(
            model_name='pergunta',
            name='enunciado',
            field=models.CharField(max_length=1000, verbose_name='Pergunta'),
        ),
        migrations.AlterField(
            model_name='pergunta',
            name='resposta_correta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bingo.resposta_correta', verbose_name='Resposta Correta'),
        ),
        migrations.AlterField(
            model_name='pergunta',
            name='resposta_incorreta',
            field=models.ManyToManyField(to='bingo.resposta_incorreta', verbose_name='Resposta Incorreta'),
        ),
    ]
