import re
from datetime import datetime, timezone, timedelta

def to_timestamp(dt_str, tz_str):
    dt = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    tz = re.match(r'(^[Uu][Tt][Cc])([+-]?[0-9]{1,2})(:00$)',tz_str)
    if tz:
        tz_utc = timezone(timedelta(hours=int(tz.group(2))))
        dt = dt.replace(tzinfo=tz_utc)
        return dt.timestamp()