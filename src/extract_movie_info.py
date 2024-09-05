import re
import json

def extract_map(html_content):
    # Define the regex pattern
    pattern = re.compile(
        r"(?P<title>.+?) \((?P<language>.+?)\) - (?P<year>\d{4}) - (?P<resolution>\d{3,4}p)? - <a href=\"(?P<url>.+?)\""
    )

    # Find all matches
    matches = pattern.finditer(html_content)

    # Extract data and convert to a list of dictionaries
    movies = []
    for match in matches:
        movie = {
            "title": match.group("title"),
            "language": match.group("language"),
            "year": match.group("year"),
            "resolution": match.group("resolution"),
            "url": match.group("url")
        }
        movies.append(movie)

    # Convert the list of dictionaries to JSON
    return movies, json.dumps(movies, indent=4)

def extract_iframe_src(html_content):  
    """Finds the `src` attribute value within an `<iframe>` element.

    Args:
        html_content (str): The HTML content to search.

    Returns:
        str: The `src` attribute value, or None if not found.
    """

    pattern = r'<iframe name="Player" ="" src="([^"]+)"'
    match = re.search(pattern, html_content)
    src = { "url": match.group(1)}
    # Convert the list of dictionaries to JSON
    return src
