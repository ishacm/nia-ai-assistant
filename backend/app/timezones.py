import pytz
from datetime import datetime

def convert_timezone(event_time, from_tz, to_tz):
    from_tz = pytz.timezone(from_tz)
    to_tz = pytz.timezone(to_tz)
    event_time = datetime.strptime(event_time, '%Y-%m-%dT%H:%M:%S')
    event_time = from_tz.localize(event_time)
    return event_time.astimezone(to_tz).strftime('%Y-%m-%dT%H:%M:%S')