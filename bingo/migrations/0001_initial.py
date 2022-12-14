# Generated by Django 4.1.3 on 2022-11-22 19:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=512)),
            ],
        ),
        migrations.CreateModel(
            name='Pergunta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bingo.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Resposta_correta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enunciado', models.CharField(max_length=1000)),
            ],
            options={
                'verbose_name': 'Resposta Correta',
            },
        ),
        migrations.CreateModel(
            name='Resposta_incorreta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enunciado', models.CharField(max_length=1000)),
            ],
            options={
                'verbose_name': 'Resposta Incorreta',
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=512)),
            ],
        ),
        migrations.CreateModel(
            name='Tabela',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pecas', models.CharField(max_length=25)),
                ('pergunta', models.ManyToManyField(to='bingo.pergunta')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bingo.usuario')),
            ],
        ),
        migrations.AddField(
            model_name='pergunta',
            name='resposta_correta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bingo.resposta_correta'),
        ),
        migrations.AddField(
            model_name='pergunta',
            name='resposta_incorreta',
            field=models.ManyToManyField(to='bingo.resposta_incorreta'),
        ),
    ]
