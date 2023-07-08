# sqlalchemy
This weather analysis uses collected weather data in beautiful Hawaii to measure and visualize percipitation and temperature data. After doing so, I also created an API using flask and python to create a small servable app to visualize this data.

The initial analysis utilizes Jupyter Notebook and the following dependencies:
- Matplotlib
- Numpy
- Pandas
- Datetime
- SQLAlchemy (automap_base, .orm Session, create_engine)

# Exploratory Analysis
Using SQLAlchemy, I created a session to reflect the data tables into an ORM. From there, I was able to do all of my exploratory analysis on the percipitation, temperature, and weather stations. 



# API creation
Next, I used a python script to initialize the following dependencies:
- SQLAlchemy (automap_base, .orm Session, create_engine)
- Flask (jsonify)
- Datetime

