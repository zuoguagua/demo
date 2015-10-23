#!/usr/bin/env python

import shelve
from datetime import datetime
from flask import Flask,request,render_template,redirect,escape,Markup

application = Flask(__name__)



DATE_FILE = 'guestbook.dat'

def save_data(name,comment,create_at):
	"""
		save the comment data
	"""
	database = shelve.open(DATE_FILE)
	
	if 'greeting_list' not in database:
		greeting_list=[]
	else:
		greeting_list = database['greeting_list']

	greeting_list.insert(0,{
		'name':name,
		'comment':comment,
		'create_at':create_at,
	})
	
	database['greeting_list'] = greeting_list
		
	database.close()



def load_data():
	database = shelve.open(DATE_FILE)
	
	greeting_list = database.get('greeting_list',[])

	database.close()
	
	return greeting_list


@application.route('/')
def index():
	greeting_list = load_data()
	return render_template('index.html',greeting_list = greeting_list)


@application.route('/post',methods=['POST'])
def post():
	name = request.form.get('name')
	comment = request.form.get('comments')
	create_at = datetime.now()
	save_data(name,comment,create_at)
	return redirect('/')
if __name__ == "__main__":
	application.run('127.0.0.1',5000,debug=True)
