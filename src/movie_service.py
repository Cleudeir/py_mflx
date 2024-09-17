import json
import os
import requests
from datetime import datetime, timedelta
from src import get_html_content, save_content, extract_movie_info, clean_text
from dotenv import load_dotenv

load_dotenv()

baseUrl = "https://redecanais.foo"
last_update_file = 'last_update.txt'
project_folder = os.path.dirname(os.path.abspath(__file__)).replace('/src', '')

def save_last_update_date():
    with open(last_update_file, 'w') as file:
        # Save the current time as Unix time (seconds since epoch) as a string
        file.write(str(datetime.now().timestamp()))


def get_last_update_date():
    if os.path.isfile(last_update_file):
        with open(last_update_file, 'r') as file:
            # Read Unix time from the file and convert it to a float
            unix_time = file.read().strip()
            return float(unix_time)
    else:
        return None

# remove all files in the json folder
def cleanCache():
    folder_path = os.path.join(project_folder, 'output/json')
    for filename in os.listdir(folder_path):
        if filename.endswith('.json'):
            os.remove(os.path.join(folder_path, filename))

def mapMovie():
    last_update = get_last_update_date()
    print(last_update)
    json_file = f'{project_folder}/output/json/map_filme.json'
    time = datetime.now().timestamp()
    if  last_update and time - last_update < 60 * 60 * 24 * 7 and os.path.isfile(json_file):
        # Return existing data if no update is needed
        with open(json_file, 'r') as file:
            movie_info = file.read()
            movie_info_json = json.loads(movie_info)
            print("Data is up to date; returning existing data.", len(movie_info_json))      
            return movie_info_json

    # Update data if it is outdated or does not exist
    url = baseUrl + "/mapafilmes.html"   
    html_content = get_html_content.get_html_content(url)
    movie_info, movie_info_json = extract_movie_info.extract_map(html_content)
    save_content.save_content('map_filme', movie_info_json, 'json')
    save_last_update_date()
    return movie_info_json

def handle_movie(urlVideo):
    name_file = clean_text.clean_text(urlVideo)
    project_folder = os.path.dirname(os.path.abspath(__file__)).replace('/src', '')
    cache_file = f'{project_folder}/output/json/{name_file}.json'
    
    if os.path.isfile(cache_file):
        with open(cache_file, 'r') as file:
            print("Data is up to date; returning existing data.")
            return json.load(file)

    movie_url = baseUrl + urlVideo
    movie_html_content = get_html_content.get_html_content(movie_url)
    iframe_src = extract_movie_info.extract_iframe_src(movie_html_content)
    iframe_src = { "url": baseUrl + iframe_src['url'] }
    result_json = json.dumps(iframe_src, indent=4)
    save_content.save_content(name_file, result_json, 'json')
    return iframe_src

def search_tmdb(type, title, year=None):
    api_key = os.getenv('TMDB_API_KEY')
    if not api_key:
        raise ValueError("API key not found in environment variables.")
    
    project_folder = os.path.dirname(os.path.abspath(__file__)).replace('/src', '')
    cache_file = f'{project_folder}/output/json/{type}_{title.replace(" ", "_")}.json'
    
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

        with open(cache_file, 'w') as file:
            json.dump(result, file, indent=4)
        
        return result
    except json.JSONDecodeError:
        return {"error": "Invalid JSON response"}
    except IndexError:
        return {"error": "No results found"}
