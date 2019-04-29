from flask import Blueprint
from flask import render_template, request, Blueprint
from flasktol.models import Question, User, Answer
from flasktol import db
main = Blueprint('main', __name__)
# home page


@main.route("/")
@main.route("/home")
def home():
    # user = User(username="kevinchen", email="kevin.chen2b2020@stu.tes.tp.edu.tw", password="$2b$12$Us0QRgN4HSLKwzlfjXSpsuPbQUd4UIbrzd8rHr5RksovTsSVUplz6", access=3)
    # db.session.add(user)
    # db.session.commit()
    return render_template("home.html")

# questions page


@main.route("/questions")
def questions():
    page = request.args.get('page', 1, type=int)
    questions = Question.query.order_by(Question.date_posted.desc()).paginate(page=page, per_page=10)
    return render_template("questions.html", title="Questions", questions=questions)
