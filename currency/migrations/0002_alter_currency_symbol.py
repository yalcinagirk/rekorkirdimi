# Generated by Django 4.2.2 on 2023-06-29 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currency',
            name='symbol',
            field=models.CharField(max_length=5),
        ),
    ]
