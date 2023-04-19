from flask import Blueprint
from flask import request, render_template
import random
from triviasite.models import Question,Movie,People,Event,Country

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

@main.route("/people",)
def people():
    active_menu = 'people' # set the active menu item
    person = People.query.first()
    primProf_filter = request.args.get('primProf_filter',None,type=str)
    year_filter = request.args.get('year_filter',None,type=str)
    if year_filter:
        year_search = f"%{year_filter[:3]}%"
    search_prof_text = "%{}%".format(primProf_filter)
    primProf_query = People.query.with_entities(People.primaryProfession).distinct().all()
    primProf_list = []
    for prof_group in primProf_query:
        for prof in prof_group[0].split(','):
            if prof not in primProf_list:
                primProf_list.append(prof)
    if (primProf_filter and year_filter):
        person = People.query.filter(People.primaryProfession.like(search_prof_text)).filter(People.birthYear.like(year_search)).first()
    elif primProf_filter:
        person = People.query.filter(People.primaryProfession.like(search_prof_text)).first()
    elif year_filter:
        person = People.query.filter(People.birthYear.like(year_search)).first()
    else:
        person = People.query.first()
    return render_template('people.html',active_menu=active_menu,person=person,primProf_list=primProf_list,primProf_filter=primProf_filter,year_filter=year_filter)

@main.route("/events")
def events():
    active_menu = 'events'
    year_filter = request.args.get('year_filter',None,type=str)

    if year_filter:
        #year_search = f"%{year_filter[:3]}%"
        year_search = str(int(year_filter) + random.randint(1, 9)) #Generate a random year from the decade selected
        events_query = Event.query.filter(Event.event_year.like(year_search)).limit(3)
        events = events_query.all()
    else:
        random_year = str(random.randint(1950, 2000))
        events_query = Event.query.filter(Event.event_year.like(random_year)).limit(3)
        events = events_query.all()
    return render_template('events.html',active_menu=active_menu,events = events,year_filter=year_filter)

@main.route("/geography")
def geography():
    active_menu = 'geography'
    country = Country.query.first()
    continent_filter = request.args.get('continent_filter',None,type=str)
    if continent_filter:
        country = Country.query.filter(Country.continent.like(continent_filter)).first()
    continents = Question.query.with_entities(Country.continent).distinct()
    return render_template('geography.html',active_menu=active_menu,country=country,continent_filter=continent_filter, continents=continents)