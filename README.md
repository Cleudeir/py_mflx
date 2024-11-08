## Project Overview

* This project is a Flask web application that fetches movie data from external APIs, processes it, and displays it on a webpage. It leverages caching to improve performance and offers features like movie searching and filtering by year.

## Dependencies

* Before you can start using or working with this project, make sure to install the following dependencies:
    * Flask
    * python-dotenv
    * flask-cors
    * requests
    * beautifulsoup4
    * urllib
    * re
    * json
    * datetime
    * os
    * dotenv

## How to Install

* To get this project up and running, follow these steps:
    1. Clone the repository.
    2. Install the required dependencies using `pip install -r requirements.txt`.
    3. Create a `.env` file in the root directory and add the following environment variable: `TMDB_API_KEY=your_api_key`. Replace `your_api_key` with your actual TMDb API key.
    4. Run the application using `docker-compose up -d`.

## How to Use

* Once you have the project set up, you can start using it in the following ways:
    1. Access the application through your web browser by navigating to `http://localhost:5000/`.
    2. Search for movies by typing in the search bar.
    3. Filter movies by year using the dropdown menu.
    4. Click on a movie card to view more details about the movie.
    5. The application will cache movie data to improve performance. This data is updated every 7 days.
    6. You can clear the cached data by running the `cleanCache` endpoint.
    7. You can view the source code of the application in the `app.py` file.
    8. The Docker Compose configuration is defined in the `docker-compose.yml` file. 
    9. The HTML templates are located in the `templates` directory.