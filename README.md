## Summary

This project consists of several Python scripts designed to build a movie information service.  The service scrapes movie data from `redecanais.foo`, retrieves additional details from the TMDB API, and caches the results for improved performance.  The data is processed using regular expressions and stored as JSON files.  A Flask application provides API endpoints to access the movie information and display it via HTML templates. The project incorporates Docker and Docker Compose for deployment and includes security measures to prevent malicious link openings in the web interface.  The overall goal is to create a comprehensive and efficient movie data management and presentation system.

## Tech Stack

Python, Flask, TMDB API, requests, BeautifulSoup, regular expressions, JSON, Docker, Docker Compose, HTML, CSS, JavaScript, Jinja2 (templating engine), `python-dotenv`
