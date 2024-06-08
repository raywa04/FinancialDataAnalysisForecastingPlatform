import React, { useEffect, useState } from 'react';
import DataTable from './components/DataTable';
import axios from 'axios';

function App() {
  const [data, setData] = useState([]);

  useEffect(() => {
    axios.get('/api/data')
      .then(response => setData(response.data))
      .catch(error => console.error('Error fetching data:', error));
  }, []);

  return (
    <div className="App">
      <h1>Financial Data Analysis and Forecasting</h1>
      <DataTable data={data} />
    </div>
  );
}

export default App;
