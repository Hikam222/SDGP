import React,{useState} from 'react';
import './Team.css';


function Team(){

const [pname] = useState('M.B.M. Hikam');
const [job] = useState('Undergraduate at University of Westminster');
const [about] = useState('Someone who enjoys finding solutions to difficult problems.');
const [p1name] = useState('Dumindu Hewarachchi');
const [job1] = useState('Undergraduate at University of Westminster');
const [about1] = useState('Someone who enjoys finding solutions to difficult problems.');
const [pname2] = useState('Sayuru Gunathikaka');
const [job2] = useState('Undergraduate at University of Westminster');
const [about2] = useState('Someone who enjoys finding solutions to difficult problems.');
const [pname3] = useState('Thamadie Gunawardana');
const [job3] = useState('Undergraduate at University of Westminster');
const [about3] = useState('Someone who enjoys finding solutions to difficult problems.');
const [pname4] = useState('Jayami Rasara');
const [job4] = useState('Undergraduate at University of Westminster');
const [about4] = useState('Someone who enjoys finding solutions to difficult problems.');
const [pname5] = useState('Tharusha Peiris');
const [job5] = useState('Undergraduate at University of Westminster');
const [about5] = useState('Someone who enjoys finding solutions to difficult problems.');


return(
    <div className='Team'>
        <h1>Team</h1>

        <div className="A-team-container">
            
            <div className="content">
                <div className="upper-container">
                    <div className="image-container">
                    <img src="user/b3.jpg" alt="Team Leader" height="100px" width="100px"/>
                    </div>
                </div>
            <div className="lower-container">
                <h3>{ pname }</h3><br/>
                <h4>{job}</h4>
                <p>{ about }</p>
                <button>Visit Profile</button>
            </div>
            </div>
            <div className="content">
                <div className="upper-container">
                    <div className="image-container">
                    <img src="user/b3.jpg" alt="Team Leader" height="100px" width="100px"/>
                    </div>
                </div>
            <div className="lower-container">
                <h3>{ p1name }</h3><br/>
                <h4>{job1}</h4>
                <p>{ about1 }</p>
                <button>Visit Profile</button>
            </div>
            </div>
            <div className="content">
                <div className="upper-container">
                    <div className="image-container">
                    <img src="user/b3.jpg" alt="Team Leader" height="100px" width="100px"/>
                    </div>
                </div>
            <div className="lower-container">
                <h3>{ pname2 }</h3><br/>
                <h4>{job2}</h4>
                <p>{ about2 }</p>
                <button>Visit Profile</button>
            </div>
            </div>
            <div className="content">
                <div className="upper-container">
                    <div className="image-container">
                    <img src="user/g3.jpg" alt="Team Leader" height="100px" width="100px"/>
                    </div>
                </div>
            <div className="lower-container">
                <h3>{ pname3 }</h3><br/>
                <h4>{job3}</h4>
                <p>{ about3 }</p>
                <button>Visit Profile</button>
            </div>
            </div>
            <div className="content">
                <div className="upper-container">
                    <div className="image-container">
                    <img src="user/g3.jpg" alt="Team Leader" height="100px" width="100px"/>
                    </div>
                </div>
            <div className="lower-container">
                <h3>{ pname4 }</h3><br/>
                <h4>{job4}</h4>
                <p>{ about4 }</p>
                <button>Visit Profile</button>
            </div>
            </div>
            <div className="content">
                <div className="upper-container">
                    <div className="image-container">
                    <img src="user/g3.jpg" alt="Team Leader" height="100px" width="100px"/>
                    </div>
                </div>
            <div className="lower-container">
                <h3>{ pname5 }</h3><br/>
                <h4>{job5}</h4>
                <p>{ about5 }</p>
                <button>Visit Profile</button>
            </div>
            </div>
        </div>
        
    </div>
);
}

export default Team;
