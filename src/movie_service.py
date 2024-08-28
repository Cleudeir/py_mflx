
import json
import os
from src import get_html_content, save_content, extract_movie_info, clean_text

baseUrl = "https://redecanais.la"

def mapMovie():
    url = baseUrl + "/mapafilmes.html"

    if os.path.exists('map_filme.json'):
        with open('map_filme.json', 'r') as file:
            html_content = file.read()
    else:
        html_content = get_html_content.get_html_content(url)
        save_content.save_content('map_filme', html_content, 'html')

    if os.path.exists('map_filme.json'):
        with open('map_filme.json', 'r') as file:
            movie_info = file.read()
            movie_info_json = json.loads(movie_info)
    else:
        movie_info, movie_info_json = extract_movie_info.extract_map(html_content)
        save_content.save_content('map_filme', movie_info_json, 'json')

    return movie_info

def handle_post_movie(movie):
    movie_url = baseUrl + movie.get('url', '')
    movie_html_content = get_html_content.get_html_content(movie_url)
    name_file = clean_text.clean_text(movie.get('title', ''))
    save_content.save_content(name_file, movie_html_content, 'html')
    iframe_src = extract_movie_info.extract_iframe_src(movie_html_content)
    
    movie['iframe_src'] = iframe_src
    movie_json = json.dumps(movie, indent=4)
    save_content.save_content(name_file, movie_json, 'json')

    return movie
