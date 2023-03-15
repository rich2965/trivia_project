from flask import Blueprint, flash, redirect, url_for, render_template, request,abort,Blueprint
from flask_login import login_required, current_user
from triviasite import db
from triviasite.models import Question
from triviasite.questions.forms import PostForm

questions = Blueprint('questions',__name__)



