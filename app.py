from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")
mongo.db.collection.drop()

@app.route("/")
def home():
    # go to home page to scrape info
    return render_template("index.html")


@app.route("/scrape")
def scrape():

    # Run the scrape function and save the results to a variable
    mars_data=scrape_mars.scrape()

    # Update the Mongo database using update and upsert=True
    mongo.db.collection.update({}, mars_data, upsert=True)

    # Redirect back to home page
    return redirect("/scrape_results")


@app.route("/scrape_results")
def result():
    # Find one record of data from the mongo database
    mision_mars = mongo.db.collection.find_one()

    # Return template and data
    return render_template("scrape_results.html", mars = mision_mars)

if __name__ == "__main__":
    app.run(debug=True)
    