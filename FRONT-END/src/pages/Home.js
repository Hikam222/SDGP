import React from 'react';
//import {PostMasonry} from '../components/common';
//import trending from '../assets/mocks/trending';
import './Home.css';
function Home() {
return (<body>
<header>
    <nav className="homenavbar">
        <div className="homecontainer">
            <a href="index.html" className="homenavbar-brand">Fabric Elastics</a>
            <div className="homenavbar-nav">
                <a href="#Home.js"> Home | </a>
                <a href="#homeblog"> Types of Elastics | </a>
                <a href="#homedesign"> Products </a>
            </div>    
        </div>
    </nav>
    <div className="homebanner">
        <div className="homecontainer">
           <h1 className="homebanner-title"> Everything you want to know about <span>Fabric  Elastic</span></h1><br/>
            <p>fabric elastic tapes are essential components in intimate apparel to provide support, hold the garment in the right position, create a finished edge, and give aesthetic effects. Applications include bra straps, elastic bands, foldover elastics, and wire channels. They can be produced by either weaving or warp knitting. Warp-knitted elastic tapes are also called crochet elastic tapes. Woven elastic tapes are usually smoother, finer, and flatter than crochet elastic tapes. Elongation, modulus, durability, handfeel, and aesthetics are the key criteria in the selection of narrow fabric elastic tapes for intimate apparel. </p>
        </div>
    </div>
</header>

<section className="homeblog" id="homeblog">
    <div className="homecontainer">
        <div className="hometitle">
            <h2>Types of Elastics</h2>
            <p>- recent types -</p>
        </div>
        <div className="homeblog-content">

            <div className="homeblog-item">
                <div className="homeblog-img">
                    <img src="./img/type1.1.jpg" alt="111"/>
                </div>
                <div className="homeblog-text">
                   
                    <h2>Braided Elastics</h2>
                    <p>Braided elastic has parallel ribs that run the length of the elastic. 
                        This type of elastic becomes more narrow as it stretches and loses stretch when it is sewn or pierced with needles and pins. 
                        For these reasons, braided elastic is ideal for using in casings, such as waistlines, sleeve hems, or necklines.</p>
                </div>
            </div>
            <div className="homeblog-item">
                <div className="homeblog-img">
                    <img src="../img/type2.1.jpg" alt=""/>
                </div>
                <div className="homeblog-text">
                    
                    <h2>Knit Elastics</h2>
                    <p>Knit elastic has a smooth appearance and is soft against the skin. 
                        Knit elastic does not become more narrow as it stretches and does not lose resiliency when sewn. 
                        Knit elastic can be used for many purposes and is best for lightweight and medium-weight fabrics.</p>
                </div>
            </div>
            <div className="homeblog-item">
                <div className="homeblog-img">
                    <img src="../img/type3.jpg" alt=""/>
                </div>
                <div className="homeblog-text">
                    
                    <h2>Woven Elastics</h2>
                    <p>Woven elastic—or “no roll”—is the strongest garment elastic.
                         This elastic is easily identified by its horizontal and vertical ribs.
                          This variety of elastic does not become more narrow as it stretches and does not lose resiliency when sewn.
                           Woven elastic is ideal for projects that use heavyweight fabrics, such as outerwear.
</p>
                </div>
            </div>
        </div>
    </div>
</section>

<section className="homedesign" id="homedesign">
    <div className="homecontainer">
        <div className="hometitle">
            <h2>     Products     </h2>
            <p>     - Recently used -    </p>
        </div>

        <div className="homedesign-content">

            <div className="homedesign-item">
                <div className="homedesign-img">
                    <img src="../img/prod1.jpg"alt=""/>
                    <span>semi-dull polyester mesh</span>
                </div>
                <div className="homedesign-title">
                    <a href="#">Material : Polyester<br/>
Ingredient : 100% polyester<br/>
Width (inch) : 60<br/>
Square meter (gram) : 140</a>
                </div>
            </div>
            <div className="homedesign-item">
                <div className="homedesign-img">
                    <img src="../img/prod2.jpg"alt=""/>
                    <span>Semi-dull nylon jersey</span>
                </div>
                <div className="homedesign-title">
                    <a href="#">Material : Nylon<br/>
Ingredient : 82% recycled nylon+ 18% Spandex<br/>
Width (inch) : 60<br/>
Square meter (gram) : 185 </a>
                </div>
            </div>
            <div className="homedesign-item">
                <div className="homedesign-img">
                    <img src="../img/prod3.jpg"alt=""/>
                    <span>Calendering super soft jersey</span>
                </div>
                <div className="homedesign-title">
                    <a href="#">Material : Polyester<br/>
Ingredient : 95% Polyester+5% Spandex<br/>
Width (inch) : 54<br/>
Square meter (gram) : 110 </a>
                </div>
            </div>
            <div className="homedesign-item">
                <div className="homedesign-img">
                    <img src="../img/prod4.jpg"alt=""/>
                    <span>Nylon BK fabric
</span>
                </div>
                <div className="homedesign-title">
                    <a href="#">Material : Nylon<br/>
Ingredient : 100% nylon<br/>
Width (inch) : 54<br/>
Square meter (gram) : 140</a>
                </div>
            </div>
            <div className="homedesign-item">
                <div className="homedesign-img">
                    <img src="../img/prod5.jpg"alt=""/>
                    <span>Semi-dull polyester jersey</span>
                </div>
                <div className="homedesign-title">
                    <a href="#">Material : Polyester<br/>
Ingredient : 88% Recycled polyester +12% Spandex<br/>
Width (inch) : 60<br/>
Square meter (gram) : 150</a>
                </div>
            </div>

        </div>
    </div>
</section>



</body>
)
}
export default Home;