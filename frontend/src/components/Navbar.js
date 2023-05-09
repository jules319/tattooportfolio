import React from 'react';
import './Navbar.css';

const Navbar = () => {
  return (
    <div className="navbar">
      <a href="/">Home</a>
      <a href="/portfolio">Portfolio</a>
      <a href="/rates">Rates & Policies</a>
      <a href="/booking">Booking</a>
    </div>
  );
};

export default Navbar;
