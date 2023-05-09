import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';

import './App.css';
import Navbar from './components/Navbar';
import HomePage from './components/HomePage';
import Portfolio from './components/Portfolio';
import RatesAndPolicies from './components/RatesAndPolicies';
import Booking from './components/Booking';


function App() {
  return (
    <div className="App">
      <Router>
        <Navbar />
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/portfolio" element={<Portfolio />} />
          <Route path="/rates" element={<RatesAndPolicies />} />
          <Route path="/booking" element={<Booking />} />
        </Routes>
      </Router>
    </div>
  );
}

export default App;
