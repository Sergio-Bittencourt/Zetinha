# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-21 18:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nu_cargo', models.IntegerField()),
                ('no_cargo', models.CharField(max_length=32, unique=True)),
                ('ic_ativo', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Entidade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nu_entidade', models.IntegerField()),
                ('co_entidade', models.CharField(max_length=32, unique=True)),
                ('no_entidade', models.CharField(max_length=32, unique=True)),
                ('sg_entidade', models.CharField(max_length=32, unique=True)),
                ('ic_ativo', models.BooleanField()),
                ('cnpj', models.IntegerField(unique=True)),
                ('telefone', models.IntegerField()),
                ('cep', models.IntegerField()),
                ('nu_municipio', models.IntegerField()),
                ('co_esfera', models.CharField(max_length=32, unique=True)),
                ('de_endereco', models.CharField(max_length=128, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Responsavel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nu_responsavel', models.IntegerField()),
                ('no_responsavel', models.CharField(max_length=32, unique=True)),
                ('cpf', models.IntegerField()),
                ('telefone', models.IntegerField()),
                ('co_matricula', models.CharField(max_length=32, unique=True)),
                ('ic_ativo', models.BooleanField()),
            ],
        ),
    ]