from flask import request, jsonify
from app.auth import authenticate_user
from app.calendar import get_calendar_events
from app.notes import get_notes, add_note
from app.llm import generate_response

@app.route('/api/query', methods=['POST'])
def handle_query():
    data = request.json
    query = data.get('query')
    user = authenticate_user(request.headers.get('Authorization'))

    if not user:
        return jsonify({'error': 'Unauthorized'}), 401

    # Fetch calendar events if needed
    if 'calendar' in query.lower():
        events = get_calendar_events(user)
        response = generate_response(query, events)
    elif 'note' in query.lower():
        notes = get_notes(user)
        response = generate_response(query, notes)
    else:
        response = generate_response(query)

    return jsonify({'response': response})

@app.route('/api/notes', methods=['POST'])
def add_user_note():
    data = request.json
    user = authenticate_user(request.headers.get('Authorization'))
    note = data.get('note')

    if not user:
        return jsonify({'error': 'Unauthorized'}), 401

    add_note(user, note)
    return jsonify({'message': 'Note added successfully'})