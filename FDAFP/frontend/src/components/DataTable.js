import React from 'react';

function DataTable({ data }) {
  return (
    <table>
      <thead>
        <tr>
          <th>Date</th>
          <th>Value</th>
          <th>Moving Average</th>
          <th>Forecast</th>
        </tr>
      </thead>
      <tbody>
        {data.map((row, index) => (
          <tr key={index}>
            <td>{row.date}</td>
            <td>{row.value}</td>
            <td>{row.moving_avg}</td>
            <td>{row.forecast}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}

export default DataTable;
