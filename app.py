from flask import Flask, render_template, jsonify

app = Flask(__name__)

jobs = [{
  'id': 1,
  'title': 'Software Engineer',
  'location': 'Banglore, India',
  'salary': '$80,000'
}, {
  'id': 2,
  'title': 'Backend Developer',
  'location': 'Mumbai, India',
  'salary': '$70,000'
}, {
  'id': 3,
  'title': 'Data Scientist',
  'location': 'tokyo, Japan',
  'salary': '$50,000'
}, {
  'id': 4,
  'title': 'Game Developer',
  'location': 'Gurugram, India',
  'salary': '$40,000'
}]


@app.route("/")
def hello_world():
  return render_template("home.html", jobs=jobs, company_name="DIV")


@app.route("/api/jobs")
def list_jobs():
  return jsonify(jobs)


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
