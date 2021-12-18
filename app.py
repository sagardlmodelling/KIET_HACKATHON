from flask import Flask

#create object with name app
app = Flask(__name__)

#create a default route and client will request on this route
@app.route('/') #this is a decorator
def home():
	return "Welcome to Ineuron"


@app.route('/about')
def about():
	return "This is Sagar Kandpal"

if __name__=="__main__":
	app.run(debug=True) #to know the error and restart web server