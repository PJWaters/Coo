![Coo](https://repository-images.githubusercontent.com/441897620/fb1db68a-ec46-4786-9c96-c1134fc7f4d6)

# Coo - F.A.R.M stack BoilerPlate
F.A.R.M - FastAPI, React, MongoDB

This boilerplate utilizes FastAPI to build a REST API, MongoDB for data storage, and React to build the front end

## Technologies
### Backend
- [FastAPI](https://fastapi.tiangolo.com/)
- [MongoDB](https://www.mongodb.com/)
- [Python 3.8](https://www.python.org/downloads/release/python-380/)
- [uvicorn](https://uvicorn.org/)

### Frontend
- [React](https://reactjs.org/)
- [Webpack](https://webpack.js.org/)
- [Babel](https://babeljs.io/)
- [NodeJS](https://nodejs.org/en/)


## Installation
### Backend
CD into the backend directory

Create a virtual environment

Install the required packages using `pip install -r requirements.txt`

Create a .env file in the backend directory and add the following variables:
- `PORT` - The port to run the server on
- `HOST` - The host IP to run the server on
- `DEBUG_MODE` - Whether or not to run the server in debug mode
- `MONGO_URI` - The URI to connect to MongoDB
- `MONGO_DB_NAME` - The name of the database to connect to

Run the server using `python main.py`

### Frontend
CD into the frontend directory

run `npm install`

Run the server using `npm run start`




