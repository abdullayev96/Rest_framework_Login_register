# Generated by Django 4.2.3 on 2023-08-04 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avtobus', '0006_rename_cat_orderpost_cats'),
    ]

    operations = [
        migrations.AddField(
            model_name='avtobusyear',
            name='title',
            field=models.TextField(default=2),
            preserve_default=False,
        ),
    ]
