from bottle import route, run, view, static_file
from datetime import datetime as dt
from random import random
from horoscope import generate_prophecies

@route('/<filename>')
def server_static(filename):
    return static_file(filename, root='\Desktop\Python\курсы\module5server')

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
   
def styles_css():
    return static_file("styles.css", root="..\styles.css")

@route("/api/forecast")
def forecast():
	return ({"predictions": generate_prophecies(),})
	


run(host="localhost", port=8080, debug=True)
