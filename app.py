import sys
import os
sys.path.append(os.path.dirname(__file__))
from tasks import easy_task, medium_task, hard_task
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return f"""
    <h2>Study Scheduler Environment</h2>
    <p>Easy: {easy_task()}</p>
    <p>Medium: {medium_task()}</p>
    <p>Hard: {hard_task()}</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7860)
