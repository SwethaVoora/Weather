# Weather
This is a weather application that retrieves weather information for different cities using the OpenWeatherMap API. 
It allows users to add cities, view their weather data, and delete cities from the list.

## Files
The project consists of the following fiels:
- **app.py** : Main Flask application file
- **\_\_init__'.py** : Contains the create app and create database function definitions
- **views.py** : This file defines the routes and handles the weather data retrieval, city addition and deletion.
- **models.py** : Contains the City Model definition used for interacting with the database.
- **templates/weather.html** : This file is responsible for displaying the weather data and handling user interactions.

## Installation
1. Clone the repository 

    ```
    git clone https://github.com/SwethaVoora/Weather.git
    ```
2. Run the flask application 'app.py' after going to the project directory
3. Open a web browser and navigate to 'http://localhost:5000' to access the applicaiton.
