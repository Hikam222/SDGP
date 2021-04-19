import React from 'react';
import './Message.css';
function Messages() {
  return (
    <div className='messages'>
      <body>
        <div className="container">
          <h1>- Contact With Us -</h1>
          <p>
            We would love to respond to your queries and help you succeed. Feel free to get in touch with us. 
          </p>
          <div className="contact-box">
            <div className="contact">
              
              <h3>Send Your Request</h3>
              
              <form method="post" action="https://formspree.io/f/mjvjkgdg">
                <div className="input-row">
                  <div className="input-group">
                    <label for="fname">Name </label>
                    <input type="text" name="fname" placeholder=" Name" required/>
                  </div>
                  <div className="input-group">
                    <label for="mobile">Phone </label>
                    <input type="text" name="mobile" placeholder=" Contact Number"/>
                  </div>
                </div>

                <div className="input-row">
                  <div className="input-group">
                    <label for="email">Email </label>
                    <input type="email" name="email" placeholder=" Email Address" required/>
                  </div>
                  <div className="input-group">
                    <label for="subject">Subject </label>
                    <input type="text" name="subject" placeholder=" Subject"/>
                  </div>
                </div>

                <label for="message">Message</label>
                <textarea rows="5" name="message" placeholder="Message"/>

                <button type="submit">SEND</button>
             </form>
            </div>


          </div>

          </div>
      </body>
      
    </div>
  );
}

export default Messages;