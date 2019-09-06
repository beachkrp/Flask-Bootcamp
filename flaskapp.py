#Imports

from flask import Flask

# Create App
app = Flask(__name__);

#Add route for the index page
@app.route('/')
def index():
	return "<h1>Hello Puppy!</h1>"
 

#Add a basic route for infoormation page
@app.route("/information")
def info():
	return "<h1> Puppies are cute</h1"

#add a dynamnic route
@app.route("/puppy/<name>")	
def puppy(name):
	return "<h1> This is a page for {} </h1>".format(name)



if __name__ == '__main__':
	app.run()
	