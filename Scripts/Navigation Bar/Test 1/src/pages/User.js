
import React from 'react';
import './User.css';


function User(){
return(
    <div className='User'>
        <h1>User</h1>
        <body div className="user-body"> 
            <center>
                <div className="box">
                <img src="b3.jpg" alt="User"/>
                    <input type="file" name="" id="file" accept="image/*"></input>
                    <label for="file">EDIT</label>
                    <input type="text" name="" placeholder="User Name"/>
                    <input type="email" name="" placeholder="Email ID"/>
                    <input type="text" name="" placeholder="PHONE NUMBER"/>
                    <input type="text" name="" placeholder="Date Of Birth"/>
                    <input type="text" name="" placeholder="GENDER"/>
                    <button className="cancel-btn">CANCEL</button>
                    <button className="done-btn">DONE</button>

                    </div>
                    <p>Select the image to edit profile details</p>
                </center>
        </body>
    </div>
);
}

export default User;
