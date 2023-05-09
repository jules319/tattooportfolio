import React from 'react';
import './HomePage.css';

const HomePage = () => {
  return (
    <div className="home-page">
      <div className="bio-section">
        <h2>About Jaden</h2>
        <p>Bio description...</p>
        <img src="path-to-headshot" alt="Jaden's headshot" />
      </div>
      <div className="store-info">
        <h3>Store Location & Hours</h3>
        <p>Address...</p>
        <p>Hours...</p>
      </div>
      <div className="contact-info">
        <h3>Contact Info</h3>
        <p>Phone: ...</p>
        <p>Email: ...</p>
      </div>
    </div>
  );
};

export default HomePage;
