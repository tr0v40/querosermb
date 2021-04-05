import os
import requests
from datetime import datetime, timedelta
import django
from decouple import config


os.environ.setdefault("DJANGO_SETTINGS_MODULE", config('DJANGO_SETTINGS_MODULE', default='querosermb.settings', cast=str))
django.setup()
from mms_api.models import CriptoValores
from mms_api.functions import converter_to_timestamp,calc_mms, converter_to_date


def populate():
        
    pairs = (
        (1, 'BRLBTC',),
        (2, 'BRLETH')
        )
    now = datetime.now()
    time_range_max = now - timedelta(365)
    for code, pair in pairs:
        data = (
            requests.get(
                'https://mobile.mercadobitcoin.com.br/v4/{}/candle?from={}&to={}&precision=1d'\
                    .format(
                        pair,
                        converter_to_timestamp(time_range_max),
                        converter_to_timestamp(now)
                    )
            )
        )
        if data.status_code == 200:
            values = data.json()
            try:
                for value in values['candles']:
                    print(converter_to_date(value['timestamp']), value['close'])
                    CriptoValores.objects.create(
                        pair=code,
                        mms_timestamp=value['timestamp'],
                        close=value['close']
                    )
            except TypeError:
                print('https://mobile.mercadobitcoin.com.br/v4/{}/candle?from={}&to={}&precision=1d'\
                    .format(
                        pair,
                        converter_to_timestamp(time_range_max),
                        converter_to_timestamp(now)
                    ))

def mms():
    for val in CriptoValores.objects.all():
        val.mms_20 = calc_mms(val.pair, val.mms_timestamp, 20)
        val.mms_50 = calc_mms(val.pair, val.mms_timestamp, 50)
        val.mms_200 = calc_mms(val.pair, val.mms_timestamp, 200)
        val.save()
        


if __name__ == "__main__":
    populate()
    mms()