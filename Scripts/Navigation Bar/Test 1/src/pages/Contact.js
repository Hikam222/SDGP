import React from 'react';
import './Message.css';
//import {db} from '../firebase';

function Contact() {
    

    
    return (
     <div className="contact-body">
        <div className='contact-title'>
            <h1>- Say Hello - </h1>
            <h2>We are always ready to serve you...!!!</h2>

        </div>

        <div className='contact-form'>
            <form id="contact-form" method="post" action="contact-form-handler.php">
                
                <input name="name" type ="text" className="form-control" placeholder="Your Name" required />
                <br/>
                <input name="email" type ="email" className="form-control" placeholder="Your Email" required />
                <br/>
                <textarea name ="message" className="form-control" placeholder="Message" row="4" required>
                </textarea>
                <br/>
                <input type="submit" className="form-control submit" value="SEND MESSAGE" />

                
                </form>
            </div>
        </div>
    );

}

export default Contact
