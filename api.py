from flask import Flask,render_template,request,redirect,url_for,session

app = Flask(__name__)
app.secret_key = 'hello'

@app.route("/")
def home():
	
    
	return render_template('home.html',title = 'home sweet home')

'''@app.route("/layout")
def layout():
	
    
	return render_template('layout.html')'''
@app.route("/about")
def about():
	
    
	return render_template('about.html',title = 'about :3')

@app.route("/contacts")
def contacts():
	
    
	return render_template('contacts.html',title = 'contacts ;)')

@app.route("/login",methods=['GET','POST'])
def login():
	if request.method == 'POST':
		users = {'user1':'123','user2':'234','user3':'1234','user4':'2345'}
		username = request.form['username']
		password = request.form['password']

		if username not in users:
			return "user doesnt exist.gobacc"

		if users[username]!=password:
			return "password nat matchin"

		session['username'] = username
		return redirect(url_for('home'))
	return redirect(url_for('home'))	

@app.route('/logout')
def logout():
	session.clear()
	return redirect(url_for('home'))

app.run(debug = True)

