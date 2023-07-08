# APIs, Apps, SQLAlchemy, and Flask
This weather analysis uses collected weather data in beautiful Hawaii to measure and visualize percipitation and temperature data. After doing so, I also created an API using flask and python to create a small servable app to visualize this data.

The initial analysis utilizes Jupyter Notebook and the following dependencies:
- Matplotlib
- Numpy
- Pandas
- Datetime
- SQLAlchemy (automap_base, .orm Session, create_engine)

# Exploratory Analysis
Using SQLAlchemy, I created a session to reflect the data tables into an ORM. From there, I was able to do all of my exploratory analysis on the percipitation, temperature, and weather stations. 

![Screen Shot 2023-07-08 at 6 35 57 PM](https://github.com/Phil-Mart/sqlalchemy/assets/120279988/985ce438-9d69-457e-ae57-67bc82178248)

![Screen Shot 2023-07-08 at 6 36 17 PM](https://github.com/Phil-Mart/sqlalchemy/assets/120279988/4e27df99-7db5-408b-b0b5-aa7bce9917be)

![Screen Shot 2023-07-08 at 6 36 52 PM](https://github.com/Phil-Mart/sqlalchemy/assets/120279988/0396f410-7125-4477-8b75-a22677adb145)



# API/APP creation
Next, I used a python script to initialize the following dependencies:
- SQLAlchemy (automap_base, .orm Session, create_engine)
- Flask (jsonify)
- Datetime

 
![Screen Shot 2023-07-08 at 6 51 52 PM](https://github.com/Phil-Mart/sqlalchemy/assets/120279988/d48456c4-3c58-40fe-bbb7-5f8d28a6f53c)

![Screen Shot 2023-07-08 at 6 37 37 PM](https://github.com/Phil-Mart/sqlalchemy/assets/120279988/dfd947be-3181-47ab-b4cd-9c07e2b279ce)


# Conclusion
With these skills, I have the capabilites to develop real ORM objects that can be served through Flask and html files. This small project is proof of concept: the ability to take data from a database and display it dynamically on the web. 
