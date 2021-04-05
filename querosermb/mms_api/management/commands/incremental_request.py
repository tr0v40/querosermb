import requests
from django.core.management.base import BaseCommand, CommandError
from mms_api.functions import today,converter_to_timestamp, calc_mms

from mms_api.models import CriptoValores

class Command(BaseCommand):
    help = 'Incremento diário da tabela CriptoValores'
    def handle(self, *args, **kwargs):
        pairs = (
                (1, 'BRLBTC',),
                (2, 'BRLETH')
                )
        now = converter_to_timestamp(today())
        # now = 1577836800
        for code, pair in pairs:
            data = (
                requests.get(
                    'https://mobile.mercadobitcoin.com.br/v4/{}/candle?from={}&to={}&precision=1d'\
                        .format(
                            pair,
                            now,
                            now
                        )
                )
            )
            if data.status_code == 200:
                values = data.json()
                try:
                    for value in values['candles']:
                        val = CriptoValores.objects.create(
                            pair=code,
                            mms_timestamp=value['timestamp'],
                            close=value['close']
                        )
                        val.mms_20 = calc_mms(val.pair, val.mms_timestamp, 20)
                        val.mms_50 = calc_mms(val.pair, val.mms_timestamp, 50)
                        val.mms_200 = calc_mms(val.pair, val.mms_timestamp, 200)
                        val.save()
                except TypeError as e:
                    print(e)