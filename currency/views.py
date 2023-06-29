from rest_framework.viewsets import ModelViewSet

from currency.models import Currency, ExchangeRate

from currency.serializers import CurrencySerializer, ExchangeRateSerializer
# Create your views here.


class CurrencyView(ModelViewSet):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer


class ExchangeRateView(ModelViewSet):
    queryset = ExchangeRate.objects.all()
    serializer_class = ExchangeRateSerializer
