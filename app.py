from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from src.movie_service import cleanCache, mapMovie, handle_movie,search_tmdb
from urllib.parse import unquote
import re

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def get():
    return {'online': 'on'}



@app.route('/movies', methods=['GET'])
def get_movies():
    movie_info = mapMovie()
    return render_template('movies.html', movies=movie_info)

@app.route('/api/clean', methods=['GET'])
def clean_cache():
    cleanCache()
    return 'Cache cleaned'
@app.route('/api/movie', methods=['GET'])
def post_movie():
    url = request.args.get('url')
    if not url:
        return jsonify({'error': 'No movie data provided'}), 400
    result = handle_movie(url)
    return result

# New endpoint to search for a movie or TV show by title and type
@app.route('/api/search', methods=['GET'])
def search_movie_or_tv():
    type = request.args.get('type')
    title = unquote(request.args.get('title'))    
    title = re.sub(r'[^a-zA-Z0-9]', ' ', title)                        
    year = request.args.get('year')
    return search_tmdb(type, title, year)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)  # Ensure it's accessible externally

