import React, { useState, useEffect } from "react";
import axios from "axios";
import "./styles.css";
import CalendarView from "./components/CalendarView";
import EventForm from "./components/EventForm";
import AnalyticsDashboard from "./components/AnalyticsDashboard";

function App() {
  const [darkMode, setDarkMode] = useState(false);
  const [events, setEvents] = useState([]);
  const [analytics, setAnalytics] = useState({});

  const toggleDarkMode = () => {
    setDarkMode(!darkMode);
  };

  useEffect(() => {
    fetchEvents();
    fetchAnalytics();
  }, []);

  const fetchEvents = async () => {
    const response = await axios.get("/api/events");
    setEvents(response.data);
  };

  const fetchAnalytics = async () => {
    const response = await axios.get("/api/analytics");
    setAnalytics(response.data);
  };

  return (
    <div className={`App ${darkMode ? "dark-mode" : ""}`}>
      <header>
        <h1>NIA - Your Neural Intelligent Aide</h1>
        <button onClick={toggleDarkMode} className="dark-mode-toggle">
          {darkMode ? "🌞 Light Mode" : "🌙 Dark Mode"}
        </button>
      </header>
      <div className="content">
        <EventForm onEventCreated={fetchEvents} />
        <CalendarView events={events} />
        <AnalyticsDashboard analytics={analytics} />
      </div>
    </div>
  );
}

export default App;