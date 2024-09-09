import json
import os
import requests
from src import get_html_content, save_content, extract_movie_info, clean_text
from dotenv import load_dotenv

load_dotenv()

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
    movie_url = baseUrl + urlVideo
    movie_html_content = get_html_content.get_html_content(movie_url)
    name_file = clean_text.clean_text(urlVideo)
    save_content.save_content(name_file, movie_html_content, 'html')
    iframe_src = extract_movie_info.extract_iframe_src(movie_html_content)
    result_json = json.dumps(iframe_src, indent=4)
    save_content.save_content(name_file, result_json, 'json')

    return iframe_src

def search_tmdb(type, title, year=None):
    api_key = os.getenv('TMDB_API_KEY')
    if not api_key:
        raise ValueError("API key not found in environment variables.")
    
    project_folder = os.path.dirname(os.path.abspath(__file__)).replace('/src', '')
    cache_file = f'{project_folder}/output/json/{type}_{title.replace(" ", "_")}.json'
    
    # Check if cache file exists
    if os.path.isfile(cache_file):
        with open(cache_file, 'r') as file:            
            return json.load(file)
    
    base_url = f"https://api.themoviedb.org/3/search/{type}"
    query = title.replace(" ", "+")
    url = f"{base_url}?query={query}&language=pt-BR"

    if type == 'movie' and year:
        url += f"&year={year}"

    headers = {
        "Authorization": f"Bearer {api_key}"
    }

    response = requests.get(url, headers=headers)
    print(url)
    
    try:
        data = response.json()
        results = data.get('results', [])
        if not results:
            result = {"error": "No results found"}
        else:
            item = results[0]
            item['backdrop_path'] = f"https://image.tmdb.org/t/p/w500{item.get('backdrop_path', '')}"
            item['poster_path'] = f"https://image.tmdb.org/t/p/w500{item.get('poster_path', '')}"
            result = item

        # Save to cache file
        with open(cache_file, 'w') as file:
            json.dump(result, file, indent=4)
        
        return result
    except json.JSONDecodeError:
        return {"error": "Invalid JSON response"}
    except IndexError:
        return {"error": "No results found"}  # Additional safeguard
