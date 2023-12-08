import React from "react";
import ecoImage1 from "../eco-environment-vector-451039.jpeg";
import ecoImage2 from "../green-planet.jpg";
import ecoImage3 from "../eco-illustration.jpg";
import { useSelector } from "react-redux";


function Home(  {isAuthenticated }) {

  const user = useSelector((state) => state.auth.user)

  return (
    <div className="home-container">
        <div className="intro-container">
        {isAuthenticated? 
        <h1>Welcome to EcoConsumer, {user.username}!</h1> : 
        <h1>Welcome to EcoConsumer!</h1>}
        
        <p>
          EcoConsumer is your gateway to a sustainable lifestyle. We believe in making eco-friendly choices accessible and enjoyable. Explore our curated content to discover the beauty of nature, understand the importance of being eco-minded, and embark on a journey towards sustainable living. Together, let's make a positive impact on our planet and create a brighter future for generations to come.
        </p>
      </div>
      <div className="home-section">
        <div className="left-div">
          <img src={ecoImage1} alt="Eco-friendly" />
        </div>
        <div className="right-div">
          <h1>Why Be Eco-Minded?</h1>
          <p>Being eco-minded is crucial for preserving our planet. Make sustainable choices to reduce your environmental impact, protect biodiversity, and create a healthier world for future generations.</p>
        </div>
      </div>

      <div className="content-container reversed">
      <div className="text-container">
        <h1>The Beauty of Nature</h1>
        <p>
          Embrace the beauty of nature by adopting eco-friendly practices. From lush forests to pristine oceans, our planet's wonders are worth preserving. Join the movement for a greener, more sustainable future.
        </p>
      </div>
      <img src={ecoImage2} alt="Eco-friendly" />
    </div>

      <div className="content-container">
        <img src={ecoImage3} alt="Eco-friendly" />
        <div className="text-container">
          <h1>Sustainable Living</h1>
          <p>
            Explore the path of sustainable living. From renewable energy to
            eco-conscious consumption, every choice you make contributes to a
            brighter, greener world. Be part of the solution for a sustainable future.
          </p>
        </div>
      </div>
      
    </div>
  );
}

export default Home;