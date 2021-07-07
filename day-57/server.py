from flask import Flask, render_template
import random
import datetime
import requests

AGE_URL = "https://api.agify.io?"
GENDER_URL = "https://api.genderize.io"
BLOG_URL = "https://api.npoint.io/3d98be9dc59684ac94d3"


app = Flask(__name__)

@app.route('/')
def home():
    random_number = random.randint(1,10)
    current_year = datetime.datetime.now().year
    return render_template("index.html", num=random_number, year=current_year)

@app.route('/guess/<name>')
def guess(name):

    gender_response = requests.get(GENDER_URL,params={"name": name})
    gender = gender_response.json()["gender"]

    age_response = requests.get(AGE_URL, params={"name": name})
    age = age_response.json()["age"]

    return render_template("name.html", name=name, age=age, gender=gender)


@app.route('/blog/<num>')
def get_blog(num):
    response = requests.get(BLOG_URL)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)

if __name__ == "__main__":
    app.run(debug=True)