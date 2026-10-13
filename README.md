
# Amazon 

This website is a clone of [Amazon](https://www.Amazon.com/).


## Table of Contents 

1. [General Info](#general-info)
2. [Wiki-Documentation](#wiki-documentation)
3. [Technologies](#technologies)
4. [Installation](#installation)
5. [Development](#development)



### General Info 
***
# Amazon
Amazon is an application where users can shop, view, comment, and purchase products that exist in the Amazon store.
* Link to live  [Amazon](https://mattsamazonclone.herokuapp.com) project. 

## Key Functionalities 

Amazon allows users to view all of the products within the store, make reviews about the products, and purchase them, which moves the users cart item directly into the the recent orders section.

  * Reviews: Users can create, read, update, and delete reviews.
  * Prime: Users can update their current Prime memebership status which offers discounts on purchase totals.
  * Products: Users can view all of the products inside of the amazon store.
  * Types: All of Amazons products are categorized into specfic types which users can view individually organized into the corresponding type.
  * Orders: Users can view their full order history and create new orders but making purchases.
  * Cart: Users can add, view, and delete cart items as desired.


### Amazon Landing Page
![landing](https://user-images.githubusercontent.com/85750283/166884515-8c58142c-e2ee-4180-ad95-1ae97366ccf9.png)


### Amazon Home Page
![home](https://user-images.githubusercontent.com/85750283/166885072-9623e28a-8e6a-499b-be6a-66564cb5cb75.png)


### Amazon Login/Signup Page 
![login](https://user-images.githubusercontent.com/85750283/166885389-4b663bf1-5ca4-4b45-86fa-4d4ec19f9756.png)
![signup](https://user-images.githubusercontent.com/85750283/166885489-8d0d367e-86c2-4b56-9e71-4ae627560c9c.png)


### Amazon Checkout page
![checkout](https://user-images.githubusercontent.com/85750283/166885240-24eeca51-a8b0-4bb0-843c-00cced962673.png)


### Amazon Drop Down Menu
![dropdown](https://user-images.githubusercontent.com/85750283/166885700-d4971397-a73d-44bc-930e-d5144650f427.png)


### Amazon Orders Page
![orders](https://user-images.githubusercontent.com/85750283/166885855-4b719b3f-793e-413e-9b4f-fbb1617cfe24.png)


### Amazon Dynamic Search
![search](https://user-images.githubusercontent.com/85750283/166886174-45fe803a-c2be-4c9c-bca3-e75dd0cf0a62.png)


### Amazon Product Page
![product](https://user-images.githubusercontent.com/85750283/166886273-1dbfd856-2709-4d4e-ab4b-0a3f0020e19d.png)

## Wiki Documentation: 
***
* [Database Schema](https://github.com/MatthewSatt/Amazon_clone/wiki/Database-Schema)
* [MVP Feature List](https://github.com/MatthewSatt/Amazon_clone/wiki/Feature-List)
* [User Stories](https://github.com/MatthewSatt/Amazon_clone/wiki/User-Stories)
* [Wireframes](https://github.com/MatthewSatt/Amazon_clone/wiki/Wire-Frames)

## Technologies
***
React 19 · Redux Toolkit · React Router 7 · Vite · Flask 3 · SQLAlchemy 2 · Alembic · PostgreSQL · Docker

## Installation

### Running with Docker (recommended)

With [Docker](https://www.docker.com/products/docker-desktop/) installed, clone the repository, cd into it, and run:

    docker compose up --build

Then open http://localhost:8000 and sign in with the demo account (`demo@aa.io` / `password`). The first start creates the Postgres database, runs the migrations, and seeds demo data. The data lives in a Docker volume, so it persists between restarts.

  •  Run Flask commands in the running container, e.g. `docker compose exec web flask seed all`

  •  `docker compose down -v` stops everything and deletes the database

### Running locally

You need Python 3.12+, Node 20.19+ and PostgreSQL.

1 ) Backend (from the repository root)

    python -m venv .venv && source .venv/bin/activate
    pip install -r requirements.txt
    cp .env.example .env        # then point DATABASE_URL at your Postgres database
    flask db upgrade
    flask seed all
    flask run -p 8000

2 ) Frontend (in a second terminal)

    cd react-app
    npm install
    npm run dev                 # http://localhost:3000, proxies /api to Flask on :8000

`npm run build` writes the production bundle to `react-app/dist`, which Flask serves.

## Development 
This project was developed by a single developer (Matthew Satterwhite).

#### Highlight features: 

* Design: Amazon was designed to be an interactive website that focuses on user experience and incorporates modern design elements. To accomplish this, transition effects and animations were added to different parts of the site to update the user on the current status of their orders, reviews, cart products, and individual payments. 



## Future Features:

• I would like to develop discounts on specific products for users that are subscribed to prime.

