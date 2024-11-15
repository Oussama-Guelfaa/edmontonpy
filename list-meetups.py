from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

# Sample data
meetups = [
    {"title": "Python Workshop", "date": datetime(2024, 12, 1)},
    {"title": "AI Conference", "date": datetime(2024, 11, 20)},
    {"title": "Hackathon", "date": datetime(2024, 11, 15)},
]

@app.route('/meetups')
def list_meetups():
    # Sort meetups by date
    sorted_meetups = sorted(meetups, key=lambda x: x["date"])
    return render_template('meetups.html', meetups=sorted_meetups)

if __name__ == '__main__':
    app.run(debug=True)