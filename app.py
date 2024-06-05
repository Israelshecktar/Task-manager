#!/usr/bin/env python3

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    task = request.form.get('task')
    if task:  # Check if the task is not an empty string
        tasks.append(task)
    return redirect(url_for('index'))

if __name__ == "__main__":
    # Correct the syntax for the IP address and the debug flag
    app.run(host="0.0.0.0", port=5000, debug=True)
