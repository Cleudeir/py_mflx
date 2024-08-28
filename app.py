from flask import Flask, request, jsonify
from src.movie_service import mapMovie, handle_post_movie

app = Flask(__name__)

@app.route('/api/movies', methods=['GET'])
def get_movies():
    movie_info = mapMovie()
    return movie_info

@app.route('/api/movies', methods=['POST'])
def post_movie():
    movie = request.json
    if not movie:
        return jsonify({'error': 'No movie data provided'}), 400

    result = handle_post_movie(movie)
    return result, 201

if __name__ == "__main__":
    app.run(debug=True)
