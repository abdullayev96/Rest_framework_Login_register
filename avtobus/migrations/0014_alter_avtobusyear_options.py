# Generated by Django 4.2.3 on 2023-08-08 07:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('avtobus', '0013_alter_avtobusyear_options_avtobusyear_body'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='avtobusyear',
            options={'ordering': ['id'], 'verbose_name': 'Avtobus haqida'},
        ),
    ]
