import firebase_admin
from firebase_admin import auth, credentials
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from google.auth.exceptions import RefreshError
import os

# Initialize Firebase
cred = credentials.Certificate('firebase-key.json')
firebase_admin.initialize_app(cred)

def authenticate_user(token):
    try:
        decoded_token = auth.verify_id_token(token)
        return decoded_token['uid']
    except:
        return None

def get_google_credentials(user_id):
    token_path = f'tokens/{user_id}.json'
    if not os.path.exists(token_path):
        return None
    creds = Credentials.from_authorized_user_file(token_path)
    if creds and creds.expired and creds.refresh_token:
        try:
            creds.refresh(Request())
        except RefreshError:
            return None
    return creds