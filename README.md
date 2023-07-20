# TDP_VISTA

Requirements:
1. - Implement a Flask API with the following endpoints:
- GET /movies/`: Retrieves movie details based on the provided movie name.
- GET /movies`: Retrieves a list of all available movies.
2. - Implement authentication using an API key. The API key should be passed as a
header in the request.
- The API key should be stored securely and not hardcoded in the application code.
- If the API key is missing or invalid, the API should return a 401 Unauthorized status
code.
3. .Integrate a free open-source movie data source:
- Use any freely available movie data source of your choice. Some examples
include:
- The Movie Database API (https://www.themoviedb.org/documentation/api)
- OMDB API (http://www.omdbapi.com/)
- IMDb API (https://imdb-api.com/)
- Register an account (if required) and obtain the necessary API credentials.
- Utilize the movie data source to fetch movie details and the movie list.
4. Return the movie details and movie list in the response:
- The `GET /movies/` endpoint should return the relevant details of the movie, such
as title, release year, plot, cast, and rating.
- The `GET /movies` endpoint should return a list of all available movies.
- The responses should be in JSON format.
5. - Ensure authentication is enforced for both endpoints (`/movies` and `/movies/`).
- If the API key is missing or invalid, the API should return a 401 Unauthorized status
code.
