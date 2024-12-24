import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';
import './styles/App.css'; // Add any styles you have, optional

// Create a root element and render the app
const root = ReactDOM.createRoot(document.getElementById('root'));

// Render the app inside React.StrictMode for additional checks during development
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
