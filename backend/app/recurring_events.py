from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

def create_recurring_event(user_id, event, recurrence_rule):
    service = build('calendar', 'v3', credentials=Credentials.from_authorized_user_file(f'tokens/{user_id}.json'))
    event['recurrence'] = [recurrence_rule]
    created_event = service.events().insert(calendarId='primary', body=event).execute()
    return created_event