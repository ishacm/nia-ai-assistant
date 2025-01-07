from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from datetime import datetime, timedelta
import pytz

def get_calendar_events(user_id):
    service = get_calendar_service(user_id)
    if not service:
        return []
    events = service.events().list(calendarId='primary').execute()
    return events.get('items', [])

def get_calendar_service(user_id):
    creds = Credentials.from_authorized_user_file(f'tokens/{user_id}.json')
    return build('calendar', 'v3', credentials=creds)

def create_event(user_id, event):
    service = get_calendar_service(user_id)
    created_event = service.events().insert(calendarId='primary', body=event).execute()
    return created_event

def edit_event(user_id, event_id, updated_event):
    service = get_calendar_service(user_id)
    updated_event = service.events().update(calendarId='primary', eventId=event_id, body=updated_event).execute()
    return updated_event

def delete_event(user_id, event_id):
    service = get_calendar_service(user_id)
    service.events().delete(calendarId='primary', eventId=event_id).execute()

def detect_conflicts(user_id, start_time, end_time):
    service = get_calendar_service(user_id)
    events = service.events().list(calendarId='primary', timeMin=start_time, timeMax=end_time).execute()
    return events.get('items', [])