from bottle import route, run, view, static_file
from datetime import datetime as dt
from random import random
from horoscope import generate_prophecies

@route("/")

@view("predictions")
def index():
	now = dt.now()
	x = random()
	return {
		"date": f"{now.day}.{now.month}.{now.year}",
		"predictions": generate_prophecies(),						
		"special_date": x > 0.5,
		"x": x,
		}

@route("/api/test")
def api_test():
   return {"test": True}
   
@route("/api/forecast")
def forecast():
	return ({"predictions": generate_prophecies(),})
	
run(host="localhost", port=8080, debug=True)
