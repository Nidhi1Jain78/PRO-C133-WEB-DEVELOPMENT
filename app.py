# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():

    name = "Nidhi jain" # write your name
    age = "15" # write your age

    return render_template('index.html' , name = name , age = age)

# define the route to father webpage
"C:/Users/KJain/Desktop/nidhi documents/whr app/PRO-C133 WEB DEVELOPMENT/family tree/templates/father.html"

# define the route to mother webpage


# define the route to friends webpage
"/friend.html"

# add other routes, if you want




# run the file
if __name__  ==  '__main__':
    app.run(debug=True)
