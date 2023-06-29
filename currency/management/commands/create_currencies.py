from django.core.management.base import BaseCommand
from currency.models import Currency
from currency.constant import currencies

class Command(BaseCommand):
    help = 'Creates default currency objects'

    def handle(self, *args, **options):
        for obj in currencies.values():
            try:
                Currency.objects.create(
                    name=obj.get("code"),
                    symbol=obj.get("symbol")
                )
            except:
                import ipdb; ipdb.set_trace()
                print("hata alınan para birimi: ", obj.get("code"),)
        print('Default currencies created successfully.')
