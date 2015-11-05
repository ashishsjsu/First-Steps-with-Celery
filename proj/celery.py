from __future__ import absolute_import
from celery import Celery
import os

app = Celery('application', include=['proj.tasks'])
app.config_from_object('celeryconfig')

if __name__ == '__main__':
	app.start()