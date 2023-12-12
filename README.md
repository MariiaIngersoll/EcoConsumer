# EcoConsumer: Your Path to Sustainable Living.

## Overview
EcoConsumer is a web application designed to be your gateway to a sustainable lifestyle. Whether you're a seasoned eco-conscious individual or just starting your journey towards sustainable living, EcoConsumer provides curated content to make eco-friendly choices accessible and enjoyable.

## Features

- **Eco-Minded Introduction:** Understand the importance of making sustainable choices in a user-friendly way.
![Eco-Minded Introduction Screenshot](screenshots_readme/Screen_Shot_2023-12-11_at_11.02.51_PM.png)

- **Product Exploration and Reviews:**

Discover Eco-Friendly Reasons: Explore the green attributes of various products, empowering you to make informed choices.

Immerse in Nature's Beauty: Learn how eco-friendly practices can bring you closer to the beauty of nature.

Guide to Sustainable Living: Gain practical insights into sustainable living and its positive impact on the environment.

- **User-Friendly Reviews:** Share your experiences by easily exploring and writing reviews for each product.

- **Visual Storytelling:** Immerse yourself in a visual journey with captivating images that highlight eco-friendliness and sustainability.

##### Install Python dependencies using Pipenv
pipenv install

##### Install Node.js dependencies for the client-side
npm install --prefix client

##### Build the client-side application for production
npm run build --prefix client

##### Navigate to the server directory
cd server

##### Apply database migrations 
flask db upgrade head

##### Seed the database with initial data
python seed.py

##### Start the Flask server for the backend 
python app.py

#### How to run this locally:

##### Start the client-side application (Frontend Server)
npm start --prefix client

##### Start the Flask Server (Backend Server)
python server/app.py

