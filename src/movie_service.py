
import json
import os
from src import get_html_content, save_content, extract_movie_info, clean_text

baseUrl = "https://redecanais.foo"

def mapMovie():
    url = baseUrl + "/mapafilmes.html"
    print(url)

    project_folder = os.path.dirname(os.path.abspath(__file__)).replace('/src', '')
    html_file = f'{project_folder}/output/html/map_filme.html'
    if os.path.isfile(html_file):
        print('html_content')
        with open(html_file, 'r') as file:
            html_content = file.read()
    else:
        html_content = get_html_content.get_html_content(url)
        save_content.save_content('map_filme', html_content, 'html')

    json_file = f'{project_folder}/output/json/map_filme.json'
    if os.path.isfile(json_file):
        with open(json_file, 'r') as file:
            movie_info = file.read()
            movie_info_json = json.loads(movie_info)
    else:
        movie_info, movie_info_json = extract_movie_info.extract_map(html_content)
        save_content.save_content('map_filme', movie_info_json, 'json')

    return movie_info

def handle_movie(urlVideo):
    movie_url = baseUrl +  urlVideo
    movie_html_content = get_html_content.get_html_content(movie_url)
    name_file = clean_text.clean_text(urlVideo)
    save_content.save_content(name_file, movie_html_content, 'html')
    iframe_src = extract_movie_info.extract_iframe_src(movie_html_content)
    result_json = json.dumps(iframe_src, indent=4)
    save_content.save_content(name_file, result_json, 'json')

    return iframe_src
