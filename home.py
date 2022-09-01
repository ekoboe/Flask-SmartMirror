from unicodedata import name
from flask import Flask, render_template, jsonify, request,flash, session, redirect, url_for
from flask_socketio import SocketIO, send
from flask_sqlalchemy import SQLAlchemy
from scripts.weather import get_weather
from scripts.CommandHandler import CommandHandler
from newsapi.newsapi_client import NewsApiClient
from scripts.asisstant import Take_query
from werkzeug.utils import secure_filename 
import os

#from scripts.widgets.NewsWidget import getnews

#from scripts.agent.classes.Listener import Listener

import datetime, requests, time
UPLOAD_FOLDER = './static/music'
ALLOWED_EXTENSIONS = {'mp3'}
app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///coba.sqlite3'
app.config['SECRET_KEY'] = "random string"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

db = SQLAlchemy(app)



socketio = SocketIO(app)  # Initialize socket api

thread = None  # Thread variable for listener

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

class tasks(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	task = db.Column(db.String(100))
	def __repr__(self):
		return f"tasks('{self.task}',)"

class music(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100))
	place = db.Column(db.String(100))
	
	def __repr__(self):
		return f"tasks('{self.music}',)"

db.create_all()
# Run the voice recording listener
# listener = Listener(name="mirror mirror")
# listener.run()

command_handler = CommandHandler()  # Create command handler object for listener


@app.route("/")
def formLogin():
	return render_template('login.html')
@app.route("/home")
def home():
	'''
	Main directory for smart mirror display
	'''
	api_key = 'bfa5fdb278474bb789ee060fdbb187f4'
	newsapi = NewsApiClient(api_key=api_key)
	top_headlines = newsapi.get_top_headlines(sources = "bbc-news")
	t_articles = top_headlines['articles']

	news = []
	desc = []
	img = []
	p_date = []

	for i in range (len(t_articles)):
		main_article = t_articles[i]

		news.append(main_article['title'])
		desc.append(main_article['description'])
		img.append(main_article['urlToImage'])
		p_date.append(main_article['publishedAt'])
    	
		contents = zip( news,desc,img,p_date)
	
	coba = tasks.query.limit(4).all()

	ms=music.query.all() 
	url=[]
	for amounts in ms:
		url.append(amounts.place)
		
	return render_template('home.html',contents=contents,coba=coba,url=url)
	
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():

	file = request.files['file']
	filename = secure_filename(file.filename)
	file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
	new_task = music(place='.'+os.path.join(app.config['UPLOAD_FOLDER'], filename),name=filename)		
	db.session.add(new_task)
	db.session.commit()	    
	return redirect(url_for('formUpload'))



@app.route("/coba")
def newsCoba():
	api_key = '25560f3cf53c433c9807c60595b373a6'
	newsapi = NewsApiClient(api_key=api_key)
	top_headlines = newsapi.get_top_headlines(sources = "bbc-news")
	t_articles = top_headlines['articles']

	news = []
	desc = []
	img = []
	p_date = []

	for i in range (len(t_articles)):
		main_article = t_articles[i]

		news.append(main_article['title'])
		desc.append(main_article['description'])
		img.append(main_article['urlToImage'])
		p_date.append(main_article['publishedAt'])
    	
		contents = zip( news,desc,img,p_date)
	
	return render_template('home.html',contents=contents)

@app.route("/update_weather", methods=['POST'])
def update_weather():
	'''
	Returns updated weather, called every 10 minutes
	'''
	currentWeather = get_weather()
	return jsonify({'result' : 'success', 'currentWeather' : currentWeather})


@app.route("/update_widget", methods=['POST'])
def update_widget():
	'''
	Returns the widget data from the assistant
	'''
	json = getnews()
	return jsonify({'result' : 'success', 'json' : json, 'widget' : 'news'})
	
# Listen for changes to the command
# def command_listener(): 

# 	prev_command = None      

# 	while True:

# 		curr_command = listener.get_command()  # Get the full phrase from the listener
# 		print(curr_command)

# 		if (curr_command != prev_command and curr_command != ""):  # Detect changes in the command
			
# 			request = command_handler.run(curr_command)
# 			socketio.emit('command', request);

# 			try:
# 				command_handler.speak()  # If the command has a script attached, speak...
# 			except:
# 				pass

# 		prev_command = curr_command  #


@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/task')
def task():
	coba = tasks.query.limit(4).all()
	return render_template('task.html',coba=coba)

@app.route('/formTask')
def formTask():
	coba = tasks.query.all()

	return render_template('formTask.html',coba=coba)

@app.route('/formUpload')
def formUpload():
	coba = music.query.all()
	return render_template('formUpload.html',coba=coba)

@app.route('/prosesTask', methods=['POST'])
def proses_task():
    task1 = request.form.get('coba')
   
    new_task = tasks(task=task1)
	
    db.session.add(new_task)
    db.session.commit()
	
    return redirect(url_for('formTask'))


@app.route('/<int:id>/deleteTask/')
def deleteTask(id):
   task=tasks.query.filter_by(id=id).one()
   db.session.delete(task)
   db.session.commit()

   return redirect(url_for('formTask'))

@app.route('/<int:id>/deleteMusic/')
def deleteMusic(id):
   musicc=music.query.filter_by(id=id).one()
   os.remove(os.path.join(app.config['UPLOAD_FOLDER'], musicc.name))
   db.session.delete(musicc)
   db.session.commit()

   return redirect(url_for('formUpload'))



@app.route('/formRegister')
def formRegister():
	return render_template('register.html')


@app.route('/registerProses', methods=['POST'])
def proses_register():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first() 

    if user: 
        flash('Email Sudah ada')
        return redirect(url_for('formRegister'))

    new_user = User(email=email, name=name, password=password)

    
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('formLogin'))

@app.route('/loginProses', methods=['POST'])
def proses_login():
    email = request.form.get('email')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first()

    
    if (user.password != password):
        flash('Please check your login details and try again.')
        return redirect(url_for('formLogin')) 
    
    session['username'] = user.name
    return redirect(url_for('index'))
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('formLogin'))


@socketio.on('connect')                                                         
def connect():                                                                  
	global thread  # Fetch the thread variable to only create one thread                                                              
	if thread is None:                                                          
		thread = socketio.start_background_task(target=command_listener)  # Run listener in background socket function


if __name__ == '__main__':
	socketio.run(app)
	Take_query()