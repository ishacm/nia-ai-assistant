from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

def get_meeting_analytics(user_id):
    service = build('calendar', 'v3', credentials=Credentials.from_authorized_user_file(f'tokens/{user_id}.json'))
    events = service.events().list(calendarId='primary', timeMin='2023-01-01T00:00:00Z').execute()
    total_meetings = len(events.get('items', []))
    return {'total_meetings': total_meetings}