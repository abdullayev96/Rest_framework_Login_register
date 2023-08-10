# Generated by Django 4.2.3 on 2023-08-05 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avtobus', '0008_alter_avtobusyear_name_alter_avtobusyear_seat_count_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CardCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='karta tarafi')),
            ],
        ),
        migrations.CreateModel(
            name='BusCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='karta nomi')),
                ('image', models.ImageField(upload_to='card/')),
                ('cat', models.ManyToManyField(blank=True, related_name='k_turlari', to='avtobus.cardcategory')),
            ],
        ),
    ]