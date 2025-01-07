import React from "react";

function CalendarView({ events }) {
  return (
    <div className="calendar-view">
      <h2>Your Schedule</h2>
      {events.map((event) => (
        <div key={event.id} className="event">
          <h3>{event.title}</h3>
          <p>{event.startTime} - {event.endTime}</p>
          <p>{event.location}</p>
        </div>
      ))}
    </div>
  );
}

export default CalendarView;