import React, { useState } from "react";
import axios from "axios";

function EventForm({ onEventCreated }) {
  const [event, setEvent] = useState({
    title: "",
    startTime: "",
    endTime: "",
    location: "",
    description: "",
  });

  const handleSubmit = async (e) => {
    e.preventDefault();
    await axios.post("/api/events", event);
    onEventCreated();
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        placeholder="Title"
        value={event.title}
        onChange={(e) => setEvent({ ...event, title: e.target.value })}
      />
      <input
        type="datetime-local"
        value={event.startTime}
        onChange={(e) => setEvent({ ...event, startTime: e.target.value })}
      />
      <input
        type="datetime-local"
        value={event.endTime}
        onChange={(e) => setEvent({ ...event, endTime: e.target.value })}
      />
      <input
        type="text"
        placeholder="Location"
        value={event.location}
        onChange={(e) => setEvent({ ...event, location: e.target.value })}
      />
      <textarea
        placeholder="Description"
        value={event.description}
        onChange={(e) => setEvent({ ...event, description: e.target.value })}
      />
      <button type="submit">Create Event</button>
    </form>
  );
}

export default EventForm;