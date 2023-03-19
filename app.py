# import flask
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify
from datetime import datetime

############
# Data Setup
############
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
Base = automap_base()

# reflect an existing database into a new model
Base.prepare(autoload_with=engine)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station


#############
# Flask Setup
#############
# create ap, pass __name__ through
app = Flask(__name__)

weather_dict = {}


#############
#Flask Routes 
#############
# Define what to do when user hits index route
@app.route("/")
def home():
    print("Server received request for 'Home' page")
    return[
        f"Welcome. Please choose from the following pages:"
        f"/api/v1.0/percipitation" 
        f"/api/v1.0/stations" 
        f"/api/v1.0/tobs"
    ]

# Define what to do when user hits the Percipitation page
@app.route("/api/v1.0/precipitation")
def percipitation():
    
    # Create our session (link) from Python to the DB
    session = Session(engine)
    
    # Calculate the date one year from the last date in data set.
    previous_year = session.query(func.date(func.max(Measurement.date), '-365 days')).scalar()

    # Perform a query to retrieve the data and precipitation scores
    rain = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= previous_year).\
        order_by(Measurement.date).all()
    
    session.close()

    # Convert the query results from your precipitation analysis (i.e. retrieve only the last 12 months of data) to a dictionary using date as the key and prcp as the value.
    pecip_dict = {}
    for date, prcp in rain:
        pecip_dict[date] = prcp

    # Return the JSON representation of your dictionary.
    return jsonify(pecip_dict)



# Define the Stations tab
@app.route("/api/v1.0/stations")
def stations():

# Return a JSON list of stations from the dataset.
    # Create our session (link) from Python to the DB
    session = Session(engine)
    station_list = session.query(Station.station, Station.name).all()

    session.close()
    
    station_dict = {}
    for station, name in station_list:
        station_dict[station] = name 
    return jsonify(station_dict)

#Define the Tobs tab
@app.route("/api/v1.0/tobs")
def tobs():    

    #Query the dates and temperature observations of the most-active station for the previous year of data.
    session = Session(engine)
    
    #Define most active station
    active_station = 'USC00519281'

    #Define one year of dates
    previous_year = session.query(func.date(func.max(Measurement.date), '-365 days')).scalar()

    #Filter and Query its tobs by date
    active_station_data = session.query(Measurement.tobs).filter(Measurement.date >= previous_year, (Measurement.station == active_station)).all()

    #Close session
    session.close()

    #Return a JSON list of temperature observations for the previous year.
    return jsonify(active_station_data)

    station_dict = {}
    for station, name in station_list:
        station_dict[station] = name 
    return jsonify(station_dict)

@app.route("/api/v1.0/<start>")
@app.route("/api/v1.0/<start>/<end>")
def search(start, end):
    
    #Query the database to collect data for input filter
    session = Session(engine)

    #Grab all Temps and dates for inquiry
    temp_days = session.query(Measurement.date, Measurement.tobs).\
        order_by(Measurement.date).all()
    temp = [temp_days[1] for tobs in temp_days]
    rain_date = [temp_days[0] for date in temp_days]

    #Define last day before closing session
    last_date = session.query(func.max(Measurement.date)).scalar()

    session.close()
    
    try:
        # Convert start and end dates to datetime objects
        start_date = datetime.strptime(start, '%Y-%m-%d')
        if end:
            end_date = datetime.strptime(end, '%Y-%m-%d')

        # For a specified start, calculate TMIN, TAVG, and TMAX for all the dates greater than or equal to the start date.    
        else:
            end_date = last_date
        
        inquiry = {}
        for date, tobs in temp_days:
            date_input = temp_days[0]


             # For a specified start date and end date, calculate TMIN, TAVG, and TMAX for the dates from the start date to the end date, inclusive.
            if start_date <= date_input <= end_date:
                min_temp = min(temp)
                max_temp = max(temp)
                avg_temp = sum(temp)/ len(temp)
                inquiry[date] = {
                    'min_temp': min_temp,
                    'max_temp': max_temp,
                    'avg_temp': avg_temp
                }
        # Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start or start-end range.
        return jsonify(inquiry)

if __name__ == '__main__':
    app.run()