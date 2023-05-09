import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';

import './App.css';
import Navbar from './components/Navbar/Navbar';
import HomePage from './components/Homepage/HomePage';
import Portfolio from './components/Portfolio/Portfolio';
import RatesAndPolicies from './components/RatesAndPolicies/RatesAndPolicies';
import Booking from './components/Booking/Booking';


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
