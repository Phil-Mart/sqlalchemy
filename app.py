# import flask
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask

#####
# Data Setup
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
Base = automap_base()



#####
# Flask Setup
# create ap, pass __name__ through
app = Flask(__name__)

weather_dict = {}


#####
#Flask Routes 
# Define what to do when user hits index route
@app.route("/")
def home():
    print("Server received request for 'Home' page")
    return("Welcome. Please choose from the following pages: Percipitation, Stations, Tobs")

# Define what to do when user hits the Percipitation page
@app.route("/api/v1.0/precipitation")
def percpipitation:
    print("Server received request for percipitation data")
    return(###)
    # Convert the query results from your precipitation analysis (i.e. retrieve only the last 12 months of data) to a dictionary using date as the key and prcp as the value.
    # Return the JSON representation of your dictionary.

# Define the Stations tab
@app.route("/api/v1.0/stations")
# Return a JSON list of stations from the dataset.

#Define the Tobs tab
@app.route("/api/v1.0/tobs")
    #Query the dates and temperature observations of the most-active station for the previous year of data.
    #Return a JSON list of temperature observations for the previous year.

@app.route("/api/v1.0/<start> and /api/v1.0/<start>/<end>")
    # Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start or start-end range.
    # For a specified start, calculate TMIN, TAVG, and TMAX for all the dates greater than or equal to the start date.
    # For a specified start date and end date, calculate TMIN, TAVG, and TMAX for the dates from the start date to the end date, inclusive.