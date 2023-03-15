from flask import Blueprint
from flask import request, render_template

from triviasite.models import Question

main = Blueprint('main',__name__)

@main.route("/")
@main.route("/home")
def home():
    page = request.args.get('page',1,type=int)
    category_filter = request.args.get('category_filter',None,type=str)
    if category_filter:
        questions = Question.query.filter_by(category=category_filter).paginate(page=page, per_page=5)
    else:
        questions = Question.query.paginate(page=page, per_page=5)
    categories = Question.query.with_entities(Question.category).distinct()
    print(request.args)
    print(category_filter)
    return render_template('home.html',questions = questions,categories=categories,category_filter=category_filter)

@main.route("/about",)
def about():
    return render_template('about.html',title = 'About')