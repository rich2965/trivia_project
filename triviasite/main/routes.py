from flask import Blueprint
from flask import request, render_template

from triviasite.models import Question,Movie

main = Blueprint('main',__name__)

@main.route("/")
@main.route("/home")
def home():
    active_menu = 'home'
    page = request.args.get('page',1,type=int)
    category_filter = request.args.get('category_filter',None,type=str)
    if category_filter:
        questions = Question.query.filter_by(category=category_filter).paginate(page=page, per_page=4)
    else:
        questions = Question.query.paginate(page=page, per_page=4)
    categories = Question.query.with_entities(Question.category).distinct()
    return render_template('home.html',active_menu=active_menu,questions = questions,categories=categories,category_filter=category_filter)

@main.route("/about",)
def about():
    active_menu = 'about' # set the active menu item
    return render_template('about.html',active_menu=active_menu,title = 'About')

@main.route("/movies",)
def movies():
    active_menu = 'movies' # set the active menu item
    movie = Movie.query.first()
    genre_filter = request.args.get('genre_filter',None,type=str)
    year_filter = request.args.get('year_filter',None,type=str)
    if year_filter:
        year_search = f"%{year_filter[:3]}%"
    search_category_text = "%{}%".format(genre_filter)
    genres_query = Movie.query.with_entities(Movie.genres).distinct().all()
    genres = []
    for genre_group in genres_query:
        for genre in genre_group[0].split(','):
            if genre not in genres:
                genres.append(genre)
    if (genre_filter and year_filter):
        movie = Movie.query.filter(Movie.genres.like(search_category_text)).filter(Movie.startYear.like(year_search)).first()
    elif genre_filter:
        movie = Movie.query.filter(Movie.genres.like(search_category_text)).first()
    elif year_filter:
        movie = Movie.query.filter(Movie.startYear.like(year_search)).first()
    else:
        movie = Movie.query.first()
    return render_template('movies.html',active_menu=active_menu,movie=movie,genres=genres,genre_filter=genre_filter,year_filter=year_filter)