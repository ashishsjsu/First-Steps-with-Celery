from __future__ import absolute_import
from proj.celery import app
import os

@app.task(bind=True)
def spark_job_task(self):
	
	task_id = self.request.id
	print "*****************************"
	print (task_id)

	master_path = 'local[2]'
	project_dir  = "/home/ashish/Desktop/"
	spark_code_path = project_dir + "wordcount.py"
	input_path = project_dir + "input.txt"
	
	result = os.system("/usr/local/spark/bin/spark-submit --master %s %s %s %s" % (master_path, spark_code_path, input_path, self.request.id))

	return {'current' : 100, 'total' : 100, 'status' : 'Task Completed!', 'result': 10, 'result': result}
