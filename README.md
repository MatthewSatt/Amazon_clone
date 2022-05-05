
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
Amazon was developed using the following Technologies: 

<img 
src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/react/react-original.svg" height=40/><img 
src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/redux/redux-original.svg" height=40/><img 
src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/flask/flask-original.svg" height=40/><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/postgresql/postgresql-original.svg"  height=40/><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/sqlalchemy/sqlalchemy-original.svg"  height=40/><img  
src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/css3/css3-original.svg"  height=40/><img  
src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original.svg"  height=40/><img  
src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/git/git-original.svg"  height=40/><img  
src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/vscode/vscode-original.svg"  height=40/>


 React | Redux | Flask | Postgres |SQLAlchemy | Alembic | CSS | Git | Node.js | NPM | HTML / JSX | Heroku

## Languages 
***

<img  src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg"  height=40/><img
src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" height=50/>
* JavaScript/React (frontend)
* Python/Flask (backend)


## Installation 

To install Amazon on your local machine please clone the project repository. 

1 )  `git clone https://github.com/MatthewSatt/Amazon_clone.git`

2 ) cd into Amazon_clone
    `cd Amazon_clone/`

3 )  Install dependencies
     
     `pipenv install --dev -r dev-requirements.txt && pipenv install -r requirements.txt`

4 )  Create a .env file based on the example with proper settings for your development environment

5 )  Setup your PostgreSQL user, password, database, and make sure it matches your .env file


  
6 ) To setup the backend application...
   
   enter the pipenv shell, migrate your database, seed your database, and run the flask application 
     
  •  `cd Amazon_clone/` 

  •  `pipenv shell` to enter the pipenv shell 

  •  `flask db upgrade`

  •  `flask seed all`

  •  `flask run` while in the shell and within the backend (Amazon_clone/) directory under localhost:5000
  
7 ) To run the frontend react application...

  •  Change into the frontend directory `Amazon_clone/react-app/`

  •  Run `npm install` to install all dependencies from the package.json within the frontend directory 
  
  •  `npm start` within the frontend directory(Amazon_clone/react-app) under localhost:3000
  
## Development 
This project was developed by a single developer (Matthew Satterwhite).

#### Highlight features: 

* Design: Amazon was designed to be an interactive website that focuses on user experience and incorporates modern design elements. To accomplish this, transition effects and animations were added to different parts of the site to update the user on the current status of their orders, reviews, cart products, and individual payments. 



## Future Features:

• I would like to develop discounts on specific products for users that are subscribed to prime.

