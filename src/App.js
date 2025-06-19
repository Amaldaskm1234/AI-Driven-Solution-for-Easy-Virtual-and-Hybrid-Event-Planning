import React, { useState } from 'react';
import './App.css';
import axios from 'axios';

function App() {
  const [eventType, setEventType] = useState('');
  const [schedule, setSchedule] = useState([]);

  const getSchedule = async () => {
    try {
      const res = await axios.post('http://localhost:5000/suggest', { event_type: eventType });
      setSchedule(res.data.schedule);
    } catch (error) {
      console.error("Error fetching schedule", error);
    }
  };

  return (
    <div style={{ padding: '2rem' }}>
      <h1>AI Event Planner 🎉</h1>
      <input
        type="text"
        placeholder="Enter event type (wedding, webinar, etc.)"
        value={eventType}
        onChange={(e) => setEventType(e.target.value)}
      />
      <button onClick={getSchedule}>Get Schedule</button>
      <ul>
        {schedule.map((item, i) => <li key={i}>{item}</li>)}
      </ul>
    </div>
  );
}

export default App;

