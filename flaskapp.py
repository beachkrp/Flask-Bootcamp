#Imports

from flask import Flask, render_template

# Create App
app = Flask(__name__);

#Add route for the index page
@app.route('/')
def index():
	return render_template("basic.html")
 

#Add a basic route for infoormation page
@app.route("/information")
def info():
	return "<h1> Puppies are cute</h1>"

#add a dynamnic route
@app.route("/puppy/<name>")	
def puppy(name):
	return "100th letter {} ".format(name[100])



if __name__ == '__main__':
	app.run(debug = True)
	