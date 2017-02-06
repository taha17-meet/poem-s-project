from flask import Flask
from databases import *
from flask import render_template , request, flash, redirect,url_for
from flask import session as login_session

app = Flask(__name__)
app.secret_key = "taha2017"

engine = create_engine('sqlite:///poems.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine, autoflush=False)
session = DBSession()
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
@app.route('/')
@app.route ('/moods')
def showMain():
 	topics = set ([poem.topic for poem in session.query(Poem).all()] + [quote.topic for quote in session.query(Quote).all()])
 	return render_template('topics.html',topics=topics)	


@app.route('/moods/<mood>')
def showByMood(mood):
 	return render_template('byMood.html', mood = mood)

@app.route('/<mood>/poems')
def showPoemsByMood(mood):
 	 poems = session.query(Poem).filter_by(topic =mood).all()
 	 return render_template('poemByMood.html', poems = poems)

@app.route('/<mood>/quotes')
def showQuotesByMood(mood):
 	quotes = session.query(Quote).filter_by(topic =mood).all()
 	return render_template('quoteByMood.html', quotes = quotes)


@app.route('/poems/<int:topic_id>')
def poems(topic_id):
	poems = session.query(Poem).filter_by(topic_id = topic_id)
	return render_template('poems.html', poems=poems)
@app.route('/quotes/<int:topic_id>')
def quotes(topic_id):
	quotes = session.query(Quote).filter_by(topic_id = topic_id)
	return  render_template('quoteByMood.html', quotes=quotes)


def verify_password(email, password):
	user = session.query(User).filter_by(email=email).first()
	if not user or not user.verify_password(password):
		return False
	else:
		return True
@app.route('/poem/<int:id>')
def showpoem(id):
	poem = session.query(Poem).filter_by(id=id).one()
	return render_template('poems.html', poem=poem)


@app.route('/newUser', methods = ['GET','POST'])
def create_account():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        if name == '' or email == '' or password == '':
            flash("Your form is missing arguments")
            return redirect(url_for('create_account'))
        if session.query(User).filter_by(email = email).first() is not None:
            flash("A user with this email address already exists")
            return redirect(url_for('create_account'))
        user = User(name = name, email=email)
        user.hash_password(password)
        session.add(user)
        session.commit()
        flash("User Created Successfully!")
        return redirect(url_for('inventory'))

    else:
        return render_template("create_account.html")

@app.route('/create_quote', methods = ['GET','POST'])
def create_quote():
    if request.method == 'POST':
        text = request.form['text']
        mood =request.form['mood']
        if session.query(Quote).filter_by(text = text).first() is not None:
            flash("A quote with this text  already exists")
            return redirect(url_for('poem_quote'))
        quote = Quote(text = text,topic = mood)
        session.add(quote)
        session.commit()
        flash("quote Created Successfully!")
        return redirect(url_for('showMain'))

    else:
        return render_template("create_quote.html")
@app.route('/create_poem', methods = ['GET','POST'])
def create_poem():
    if request.method == 'POST':
        name = request.form['name']
        text = request.form['text']
        mood = request.form['mood']

        if session.query(Poem).filter_by(text = text,name = name).first() is not None:
            flash("A poem with this text/name  already exists")
            return redirect(url_for('poem_quote'))
        poem = Poem(text = text, name=name , topic = mood)
        session.add(poem)
        session.commit()
        flash("poem Created Successfully!")
        return redirect(url_for('showMain'))

    else:
        return render_template("create_poem.html" )       




@app.route("/deletepoem/<int:poem_id>")
def deletePoem(poem_id):
	poem = session.query(Poem).filter_by(id=poem_id).one()
	session.delete(poem)
	session.commit()
	flash("Deleted poem successfully!")
	return redirect(url_for('showMain'))
@app.route("/edit/<int:poem_id>", methods = ['GET', 'POST'])   
def editPoem(poem_id):
    poem = session.query(Poem).filter_by(id=poem_id).one()
    if request.method == 'GET':
        return render_template('edit_poem.html', poem=poem)
    elif request.method == 'POST':
        poem.name = request.form['name']
        poem.topic = request.form['mood']
        poem.text = request.form['text']
        session.add(poem)
        session.commit()
        flash("Successfully edited poem!")
        return redirect(url_for('showpoem', id=poem.id))


    



@app.route("/deletequote/<int:quote_id>")
def deleteQuote(quote_id):
    quote = session.query(Quote).filter_by(id=quote_id).one()
    session.delete(quote)
    session.commit()
    flash("Deleted quote successfully!")
    return redirect(url_for('showMain'))






@app.route('/login', methods = ['GET', 'POST'])
def login():
	if request.method == 'GET':
		return render_template('login.html')
	elif request.method == 'POST':
		email = request.form['email']
		password = request.form['password']
		if email is None or password is None:
			flash('Missing Arguments')
			return redirect(url_for(login))
		if verify_password(email, password):
			user = session.query(User).filter_by(email=email).one()
			flash('Login Successful, welcome, %s' % user.name)
			login_session['name'] = user.name
			login_session['email'] = user.email
			login_session['id'] = user.id
			return redirect(url_for('index'))
		else:
			# incorrect username/password
			flash('Incorrect username/password combination')
			return redirect(url_for('login'))



if __name__=='__main__':
	app.run(debug=True)
