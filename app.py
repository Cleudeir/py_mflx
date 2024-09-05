from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from src.movie_service import mapMovie, handle_movie

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def get():
    return {'online': 'on'}

@app.route('/web/movies', methods=['GET'])
def get_movies():
    movie_info = mapMovie()
    # Render the external HTML file with movie data
    return render_template('movies.html', movies=movie_info)

@app.route('/api/movie', methods=['GET'])
def post_movie():
    url = request.args.get('url')
    if not url:
        return jsonify({'error': 'No movie data provided'}), 400

    result = handle_movie(url)
    return result

if __name__ == "__main__":
    app.run(debug=True)
