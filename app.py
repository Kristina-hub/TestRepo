# --------------------------------------- #
#       Authors: Kristina Kacmarova       #
#                Miranda Postma       	  #
#                Ridwan Bari              #
#                Winston Herold           #
#       Python Version: 3.7.4             #
#       Created on: 2022-01-18            #
# --------------------------------------- #

#flask --version
from flask import Flask, render_template, request, url_for, redirect, jsonify
from flask.globals import request
app = Flask(__name__)
# app = Flask(__name__,
#             static_url_path='', 
#             static_folder='/var/www/TestRepo/static',
#             template_folder='/var/www/TestRepo/templates')

'''---------------From file.py import class----------------'''

from read_file import ReadFile
#from static.py.read_file import ReadFile					
#from static.py.extract_dates import ExtractDates
#from static.py.output import Output


'''---------------Render pages----------------'''

@app.route('/', methods=['GET', 'POST'])
def home():
	return render_template('home.html')

@app.route('/about/',  methods=['GET', 'POST'])
def about():
	return render_template('about.html')
	
@app.route('/tutorial/',  methods=['GET', 'POST'])
def tutorial():
	return render_template('tutorial.html')
	
@app.route('/contact/',  methods=['GET', 'POST'])
def contact():
	return render_template('contact.html')


'''---------------Actions----------------'''

@app.route('/upload', methods=['POST'])
def upload():
 	f = request.files['new_file'] 
 	text = ReadFile.read_func(f)
 	#dates = ExtractDates.dates_func(text)
 	#Output.output_func(dates)
 	#message = text + "<br/>" + dates
 	message = "test"
 	return message
	
	
'''
how to run locally:
export FLASK_APP="app.py"
flask run
http://127.0.0.1:5000/
command shift R to reload static files
'''


'''
references:
https://www.pexels.com/photo/clipboard-with-calendar-placed-on-desk-amidst-stationery-6408282/

https://www.pexels.com/photo/composition-of-teapot-and-plant-twig-on-book-4271259/
https://www.pexels.com/photo/composition-of-white-mug-and-notebooks-4271257/
https://www.pexels.com/photo/notebooks-on-desk-with-ceramic-mug-4271258/

https://www.pexels.com/photo/ferns-and-flowers-surrounding-a-calendar-5498340/
https://www.pexels.com/photo/white-printer-paper-on-white-table-5499129/
https://www.pexels.com/photo/white-printer-paper-on-white-printer-paper-5498383/
https://www.pexels.com/photo/white-paper-on-green-table-5499139/

https://www.pexels.com/photo/close-up-shot-of-a-spiral-notebook-beside-a-cup-6690218/
https://www.pexels.com/photo/close-up-shot-of-a-pen-on-planner-6690208/
https://www.pexels.com/photo/flatlay-photo-of-weekly-planner-6690924/
https://www.pexels.com/photo/close-up-shot-of-weekly-planner-6690930/

https://www.svgrepo.com/svg/4336/calendar
https://realfavicongenerator.net/
'''



# from flask import Flask
# app = Flask(__name__)
# @app.route("/")
# def hello():
#     return "Hello world!"