from datetime import datetime, timedelta

from .models import CriptoValores


def mms_days(timestamp=None, mms_range=None):
    if timestamp and mms_range:
        timestamp = datetime.fromtimestamp(timestamp)
        return sorted(set(timestamp - timedelta(x) for x in range(mms_range)))
    return None

def calc_mms(pair, timestamp, mms_range):
    if pair and timestamp and mms_range:
        mms_value = 0
        objs = []
        days = mms_days(timestamp, mms_range)
        for day in days:
            try:
                objs.append(CriptoValores.objects.get(
                                                        pair=pair, 
                                                        mms_timestamp=datetime.timestamp(day)
                                                    ).close)
            except CriptoValores.DoesNotExist as e:
                print(e, day)
                return None
        if len(objs) == mms_range:
            for obj in objs:
                mms_value += obj
            return round(mms_value/mms_range, 5)
        