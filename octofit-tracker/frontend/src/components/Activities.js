import React, { useEffect, useState } from 'react';

const Activities = () => {
  const [activities, setActivities] = useState([]);
  const codespace = process.env.REACT_APP_CODESPACE_NAME;
  const endpoint = codespace
    ? `https://${codespace}-8000.app.github.dev/api/activities/`
    : 'http://localhost:8000/api/activities/';

  useEffect(() => {
    fetch(endpoint)
      .then(res => res.json())
      .then(data => {
        const results = data.results || data;
        console.log('Fetched activities:', results);
        setActivities(results);
      })
      .catch(err => console.error('Error fetching activities:', err));
    console.log('Activities endpoint:', endpoint);
  }, [endpoint]);

  return (
    <div>
      <h2 className="my-4">Activities</h2>
      <div className="table-responsive">
        <table className="table table-striped table-bordered">
          <thead className="table-dark">
            <tr>
              <th>#</th>
              <th>User</th>
              <th>Workout</th>
              <th>Date</th>
              <th>Duration (min)</th>
              <th>Calories Burned</th>
            </tr>
          </thead>
          <tbody>
            {activities.map((activity, idx) => (
              <tr key={activity.id || idx}>
                <td>{idx + 1}</td>
                <td>{activity.user?.name || ''}</td>
                <td>{activity.workout?.name || ''}</td>
                <td>{activity.date ? new Date(activity.date).toLocaleString() : ''}</td>
                <td>{activity.duration_minutes}</td>
                <td>{activity.calories_burned}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default Activities;
