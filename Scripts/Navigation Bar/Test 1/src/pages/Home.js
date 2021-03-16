import React from 'react';
function Home() {
return (
<div className='home'>

   <div className="content">
     
      <h1>Elastic Prediction System</h1><br/>
      <p>
      WOVEN FABRIC (WF) composites form one of the important classes of textile WF composites.
          They offer certain advantages over conventional unidirectional(UD)
           laminated composites which have made them attractive for structural ap-plications. 
          Complicated shapes can be obtained by using WF composites.It is easier to build thick laminates with woven fabrics than with UD tapes. 
           Thehandling of woven fabrics is easier.Therefore, the labour in making thicklaminates is also reduced. 
           WF composites also offer higher impact resistance,toughness and dimensional stability. 
           The elastic analysis of WF composites is necessary since the advantages are obtained at the cost of in-plane stiffness prop-erties.
           <div className="image">
         <img className='form-img' src='img/b15.jpg' alt='home page' />
         <img className='form-img2' src='img/p2.jpg' alt='home page' />
         <img className='form-img3' src='img/w1.jpg' alt='home page' />
         <img className='form-img4' src='img/bg.jpg' alt='home page' />
            </div>
            <div className="buttons">
            <button className="btn3">About Us</button> 
      <button className="btn2">Help</button> 
               </div>
         </p>
         
            
     </div>
</div>
);
}
export default Home;
