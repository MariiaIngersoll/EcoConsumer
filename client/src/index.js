import React from "react";
import App from "./components/App";
import "./index.css";
import { createRoot } from "react-dom/client";
import { BrowserRouter as Router } from "react-router-dom";
import { store } from "./redux_store/store"
import { Provider } from "react-redux";


<meta name="viewport" content="width=device-width, initial-scale=1.0"></meta>
const container = document.getElementById("root");
const root = createRoot(container);
root.render(
  <Router>
    <Provider store={store} >
      <App />
    </Provider>
  </Router>
);
