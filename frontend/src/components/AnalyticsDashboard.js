import React from "react";

function AnalyticsDashboard({ analytics }) {
  return (
    <div className="analytics-dashboard">
      <h2>Analytics</h2>
      <p>Total Meetings: {analytics.total_meetings}</p>
    </div>
  );
}

export default AnalyticsDashboard;