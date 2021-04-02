from datetime import datetime, timedelta, date

def mms_days(timestamp, mms):
    timestamp = date.fromtimestamp(timestamp)
    return sorted(set(timestamp - timedelta(x) for x in range(mms)))

