from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

def set_reminder(user_id, event_id, reminder_time):
    service = build('calendar', 'v3', credentials=Credentials.from_authorized_user_file(f'tokens/{user_id}.json'))
    event = service.events().get(calendarId='primary', eventId=event_id).execute()
    event['reminders'] = {'useDefault': False, 'overrides': [{'method': 'popup', 'minutes': reminder_time}]}
    updated_event = service.events().update(calendarId='primary', eventId=event_id, body=event).execute()
    return updated_event