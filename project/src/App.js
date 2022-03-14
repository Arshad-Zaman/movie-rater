/* eslint-disable react/jsx-filename-extension */
/* eslint-disable no-undef */
import React, { useState, useEffect } from 'react';

function App() {
  const [data, setData] = useState([{}]);
  const [msg, setMsg] = useState('Welcome');

  useEffect(() => {
    fetch('/load_comments').then(
      (res) => res.json(),
    ).then(
      (dbData) => {
        setData(dbData);
      },
    );
  }, []);

  const deleteClick = (id) => {
    const updatedData = data.filter((reviews) => reviews.id !== id);
    setData(updatedData);
  };

  async function saveChanges() {
    const response = await fetch('/recieve_data', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json', // The type of data you're sending
      },
      body: JSON.stringify(data), // The data
    });

    if (response.ok) {
      setMsg('Your reviews have been updated!');
    }
  }

  return (
    <div>
      <h1 className="title is-1">{msg}</h1>
      <table className="table is-fullwidth">
        <thead>
          <tr>
            <th>Movie ID</th>
            <th>Rating</th>
            <th>Comment</th>
            <th>Delete</th>
          </tr>
        </thead>
        {
      data.map((reviews) => (
        <tr key={reviews.id}>
          <td>
            Movie ID:
            {reviews.movie_id}
          </td>
          <td>{reviews.rating}</td>
          <td>{reviews.comment}</td>
          <td><button type="button" onClick={() => deleteClick(reviews.id)}>Delete</button></td>
        </tr>
      ))
    }
        <tfoot>
          <th>
            <button type="button" onClick={saveChanges}>Save changes!</button>
          </th>
        </tfoot>
      </table>
    </div>
  );
}

export default App;
