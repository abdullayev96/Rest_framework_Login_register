# Generated by Django 4.2.3 on 2023-07-28 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_senduser_reference_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='senduser',
            name='status',
            field=models.CharField(choices=[('new', 'new'), ('execution', 'execution'), ('completed', 'completed')], default='new', max_length=9),
        ),
    ]
