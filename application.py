from __future__ import absolute_import
from flask import Flask, request, session, flash, redirect, url_for, jsonify
import os

app = Flask(__name__)


@app.route('/sparktask', methods=["POST"])
def sparktask():

	from proj.tasks import spark_job_task 
	
	task = spark_job_task.apply_async()

	return jsonify({'task_id': task.id}), 202, {'Location': url_for('taskstatus', task_id=task.id)}


@app.route('/status/<task_id>')
def taskstatus(task_id):
	    
    task = spark_job_task.AsyncResult(task_id)

    return jsonify(task.state)


if __name__== '__main__':
	app.run(debug=True)