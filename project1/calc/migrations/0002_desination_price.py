# Generated by Django 4.1.4 on 2023-01-11 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='desination',
            name='price',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
