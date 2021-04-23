import React from 'react';
import './Message.css';
import * as FaIcons from 'react-icons/fa';
import Navbar from "../../Side bar/Navbar";

function Messages() {
  return (
      <div>
        <Navbar/>

    <div className='messages'>
      <body>
        <section className="contact">
          <div className="content">
            <h1>- Contact Us -</h1>
            <p>
            We would love to respond to your queries and help you succeed. Feel free to get in touch with us. 
            </p>
          </div>
          <div className="container">
            <div className="contactInfo">
              <div className="box">
                <div className="icon"><FaIcons.FaMapMarkerAlt /></div>
                  <div className="text">
                    <h3>Address</h3>
                    <p>Borella Cross Rd,<br/> Colombo 01000</p>
                  </div>
              </div>
              <div className="box">
                <div className="icon"><FaIcons.FaPhoneAlt /></div>
                  <div className="text">
                    <h3>Phone</h3>
                    <p>+94 775 220 806</p>
                  </div>
              </div>
              <div className="box">
                <div className="icon"><FaIcons.FaEnvelopeOpenText /></div>
                  <div className="text">
                    <h3>Email</h3>
                    <p>hikam.2018419@iit.ac.lk</p>
                  </div>
              </div>
            </div>
            <div className="contactForm">
              <form method="post" action="https://formspree.io/f/mjvjkgdg">
                <h2> Send Message </h2>
                <div className="inputBox">
                <label for="fname"> </label>
                  <input type="text" name="fname" required="required" />
                  <span>Full Name</span>
                </div>
                <div className="inputBox">
                <label for="email"> </label>
                  <input type="text" name="email" required="required" />
                  <span>Email</span>
                </div>
                <div className="inputBox">

                  <label htmlFor="message"> </label>
                  <textarea name="message" required="required"></textarea>
                  <span>Type Your Message...</span>

                </div>
                <div className="inputBox">
                
                  <input type="submit" name="" value="Send" />
                </div>
              </form>
            </div>
          </div>
        </section>
      </body>
      
    </div>
      </div>
  );
}

export default Messages;
