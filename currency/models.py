from django.db import models

# Create your models here.


class Currency(models.Model):
    name = models.CharField(max_length=50, unique=True) 
    symbol = models.CharField(max_length=5, unique=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ExchangeRate(models.Model):
    source_currency = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name='source_rates')  # Kaynak para birimi
    target_currency = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name='target_rates')  # Hedef para birimi
    rate = models.DecimalField(max_digits=10, decimal_places=4)  # Dönüşüm oranı
    last_updated = models.DateTimeField(auto_now=True)  # Son güncelleme tarihi

    def __str__(self):
        return f"{self.source_currency} to {self.target_currency}: {self.rate}"
