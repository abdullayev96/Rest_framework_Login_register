# Generated by Django 4.2.3 on 2023-08-01 10:50

from django.db import migrations, models
import user.models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_alter_senduser_verification_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='senduser',
            name='reference_number',
            field=models.SmallIntegerField(validators=[user.models.validate_number]),
        ),
    ]