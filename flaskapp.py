#Imports

from flask import Flask

# Create App
app = Flask(__name__);

#Add route for the index page
@app.route('/')
def index():
	return "<h1>Hello Puppy!</h1>"



if __name__ == '__main__':
	app.run()
	