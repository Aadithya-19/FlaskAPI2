import csv

from flask import Flask, json, jsonify, request

all_movies = []


with open('movies.csv', encoding="utf8") as f:

    csv_reader = csv.reader(f)

    data = list(csv_reader)

    all_movies = data[1:]

liked_movies = []

disliked_movies = []

unwatched = []



app = Flask(__name__)

@app.route("/get-movie")
def get_movie():
    movie_data = {
        "title": all_movies[0][19],
        "poster_link": all_movies[0][27],
        "release_date": all_movies[0][13] or "N/A",
        "duration": all_movies[0][15],
        "rating": all_movies[0][20],
        "overview": all_movies[0][9]
    }
    return jsonify({
        'data':all_movies[0],
        'message': "success"
    })

@app.route("/liked-movie", methods = ["POST"])
def liked_movie():
    movie = all_movies[0]
    all_movies = all_movies[1:]
    liked_movies.append(movie)
    return jsonify({
         'message':"success"
    }), 201


@app.route("/unliked-movie", methods = ["POST"])
def unliked_movie():
    movie = all_movies[0]
    all_movies = all_movies[1:]
    disliked_movies.append(movie)
    return jsonify({
         'message':"success"
    }), 201



@app.route("/unwatched-movie", methods = ["POST"])
def unwatched():
    movie = all_movies[0]
    all_movies = all_movies[1:]
    unwatched.append(movie)
    return jsonify({
         'message':"success"
    }), 201

@app.route("/popular-movies")
def popular_movies():
    movie_data = []
    for movie in output:
        _d = {
            "title": movie[0],
            "poster_link": movie[1],
            "release_date": movie[2] or "N/A",
            "duration": movie[3],
            "rating": movie[4],
            "overview": movie[5]
        }
        movie_data.append(_d)
    return jsonify({
        "data": movie_data,
        "status": "success"
    }), 200

@app.route("/recommended-movies")
def recommended_movies():
    all_recommended = []
    for liked_movie in liked_movies:
        output = get_recommendations(liked_movie[19])
        for data in output:
            all_recommended.append(data)
    import itertools
    all_recommended.sort()
    all_recommended = list(all_recommended for all_recommended,_ in itertools.groupby(all_recommended))
    movie_data = []
    for recommended in all_recommended:
        _d = {
            "title": recommended[0],
            "poster_link": recommended[1],
            "release_date": recommended[2] or "N/A",
            "duration": recommended[3],
            "rating": recommended[4],
            "overview": recommended[5]
        }
        movie_data.append(_d)
    return jsonify({
        "data": movie_data,
        "status": "success"
    }), 200

if (__name__ == "__main__"):
   app.run() 