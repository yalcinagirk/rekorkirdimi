# Generated by Django 4.2.2 on 2023-06-29 11:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('symbol', models.CharField(max_length=5, unique=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ExchangeRate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.DecimalField(decimal_places=4, max_digits=10)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('source_currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='source_rates', to='currency.currency')),
                ('target_currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='target_rates', to='currency.currency')),
            ],
        ),
    ]
