from django.urls import path

from currency.views import CurrencyView, ExchangeRateView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', CurrencyView, basename='api')
router.register(r'exchange_rate', ExchangeRateView, basename='exchange_rate')
urlpatterns = router.urls
