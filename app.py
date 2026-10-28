
from flask import Flask, render_template

app = Flask(__name__)

movies = [
    {"name": "Interstellar", "genre": "Sci-Fi", "rating": 8.7},
    {"name": "Inception", "genre": "Thriller", "rating": 8.8},
    {"name": "3 Idiots", "genre": "Comedy", "rating": 8.4},
    {"name": "RRR", "genre": "Action", "rating": 8.0},
    {"name": "Hi Nanna", "genre": "Romance", "rating": 8.2},
    {"name": "The Dark Knight", "genre": "Action", "rating": 9.0}
]

@app.route("/")
def home():
    return render_template("index.html", movies=movies)

if __name__ == "__main__":
    app.run(debug=True)
