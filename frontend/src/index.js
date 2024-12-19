import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App";
import "./styles/App.css"; // Add any styles you have, optional

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
