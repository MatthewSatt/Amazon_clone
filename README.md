
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
  * Types: All of Amazons products are categorized into specfic types which users can view their 
  * Orders: Users can view their full order history and create new orders but making purchases.
  * Cart: Users can add, view, and delete cart items them as desired.


### Amazon Landing Page
![landing](https://user-images.githubusercontent.com/85750283/155817655-01f031e4-934c-4932-8bc1-977fd5d0b7ba.png)


### Amazon Home Page
![home](https://user-images.githubusercontent.com/85750283/155817904-0443d4b2-86a2-4e53-ae9e-a3b9a26f93da.png)


### Amazon Login Page 
![login](https://user-images.githubusercontent.com/85750283/155817746-41b01f0b-a0e1-4272-aa30-51afccc114ea.png)


### Amazon Sign Up Page
![sign-up](https://user-images.githubusercontent.com/85750283/155817849-58e12c17-d83c-4355-b08d-b8ef8334c5db.png)


### Amazon Checkout page
![songs-modal](https://user-images.githubusercontent.com/85750283/155818076-8a5fcae7-28e0-45d0-934e-814a288c6880.png)


### Amazon Drop Down Menu
![songs-modal](https://user-images.githubusercontent.com/85750283/155818076-8a5fcae7-28e0-45d0-934e-814a288c6880.png)


### Amazon Drop Down Menu
![songs-modal](https://user-images.githubusercontent.com/85750283/155818076-8a5fcae7-28e0-45d0-934e-814a288c6880.png)


### Amazon Drop Down Menu
![songs-modal](https://user-images.githubusercontent.com/85750283/155818076-8a5fcae7-28e0-45d0-934e-814a288c6880.png)

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

