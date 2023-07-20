from flask import Flask, request, jsonify, abort
import requests

app = Flask(__name__)

# Hardcoded API key for simplicity
API_KEY = "3cd00e9a"

# API endpoint to retrieve movie details by name
@app.route('/movies/<string:name>', methods=['GET'])
def get_movie_details(name):
    if not validate_api_key(request.headers.get('Authorization')):
        abort(401, 'Invalid API key')

    # Make a request to the OMDB API
    response = request.get(f'http://www.omdbapi.com/?t={name}&apikey={API_KEY}')

    if response.status_code == 200:
        movie_data = response.json()
        return jsonify(movie_data)
    else:
        abort(404, 'Movie not found')

# API endpoint to retrieve the top 50 movies
@app.route('/movies', methods=['GET'])
def get_top_movies():
    if not validate_api_key(request.headers.get('Authorization')):
        abort(401, 'Invalid API key')

    movie_list = []
    page = 1

    while len(movie_list) < 50:
        # Make a request to the OMDB API with pagination
        response = request.get(f'http://www.omdbapi.com/?s=*&type=movie&page={page}&apikey={API_KEY}')

        if response.status_code == 200:
            data = response.json()
            movies = data.get('Search', [])
            if len(movies) == 0:
                break  # No more movies available

            movie_list.extend(movies)
            page += 1
        else:
            abort(500, 'Internal server error')

    return jsonify(movie_list[:50])  # Return only the first 50 movies

# Validate the API key
def validate_api_key(api_key):
    return api_key == API_KEY

if __name__ == '__main__':
    app.run(debug=True)