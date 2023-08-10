# Generated by Django 4.2.3 on 2023-08-04 10:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='cat nomi')),
            ],
        ),
        migrations.CreateModel(
            name='IpModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='vakansiya yonalishi')),
                ('experience', models.CharField(max_length=300, verbose_name='Ish tajribasi')),
                ('title', models.TextField()),
                ('number', models.CharField(max_length=50, verbose_name='tel nomer')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vacancy.category')),
                ('views', models.ManyToManyField(blank=True, related_name='soni', to='vacancy.ipmodel')),
            ],
        ),
    ]