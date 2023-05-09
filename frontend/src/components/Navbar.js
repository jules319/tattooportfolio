import React from 'react';
import './Navbar.css';
import { Link } from 'react-router-dom';


const Navbar = () => {
    return (
      <div className="navbar">
        <Link to="/">Home</Link>
        <Link to="/portfolio">Portfolio</Link>
        <Link to="/rates">Rates & Policies</Link>
        <Link to="/booking">Booking</Link>
      </div>
    );
  };
  

export default Navbar;
