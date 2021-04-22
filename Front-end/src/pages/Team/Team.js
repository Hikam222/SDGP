import React from 'react';
import './Team.css';
import Navbar from "../../Side bar/Navbar";


function Team(){
return(
    <div>
      <Navbar/>

    <div className='Team'>
        <body>
        <div className="wrapper">
            
            <h1>- Our Tech Team -</h1>

            <div className="team1">
                <div className="team-member">
                    <div className="team-img">
                        <img src="/user/hikam.jpg" alt="team_member_image" />
                    </div>
                    <h3>M.B.M.Hikam</h3>
                    <p className="role">Data science Developer </p>
                    <p>  Have a wide range of technical competencies including: statistics and machine learning, coding languages, databases, machine learning, and reporting technologies.
                        </p>
                </div>
                <div className="team-member">
                <div className="team-img">
                        <img src="/user/dumindu.jpg" alt="team_member_image" />
                    </div>
                <h3>Dumindu Hewarachchi</h3>
                    <p className="role">Backend Developer </p>
                    <p>Someone who builds and maintains the technology needed to power the components which enable the user-facing side of the website to exist.</p>
                </div>
                <div className="team-member">
                <div className="team-img">
                        <img src="/user/sayuru.jpg" alt="team_member_image" />
                    </div>
                <h3>Sayuru Gunathilaka</h3>
                    <p className="role">Frontend Developer </p>
                    <p>Providing high impact web solutions for diverse industry organizations. 
                        Skilled in designing, developing web-based applications incoperating a range of technologies. </p>
                </div>
                </div>
               
                <div className="team2">
                <div className="team-member">
                <div className="team-img">
                        <img src="/user/jayami.jpg" alt="team_member_image" />
                    </div>
                    <h3>Jayami Rasara</h3>
                    <p className="role">Data science Developer </p>
                    <p>Utilize analytical, statistical, and programming skills to collect, analyze, and interpret large data sets.
                    Proficient in statistical models with R and Python.</p>
                </div>
                <div className="team-member">
                <div className="team-img">
                        <img src="/user/thamadie6.png" alt="team_member_image" />
                    </div>
                <h3>Thamadie Gunawardane</h3>
                    <p className="role">Backend Developer </p>
                    <p>Responsible for preparing all the information that needs to be sent over to be used on the client-facing side of the web browser.</p>
                </div>
                <div className="team-member">
                <div className="team-img">
                        <img src="/user/tharusha.jpg" alt="team_member_image" />
                    </div>
                <h3>Tharusha Peiris</h3>
                    <p className="role">Frontend Developer </p>
                    <p>Innovative Frontend Developer that maintains responsive websites in the recruiting industry.
                        Proficient in HTML, CSS, Javascript and modern frameworks.
                    </p>
                </div>
                
            </div>        
        </div>
        </body>
        </div>
    </div>
);
}

export default Team;
