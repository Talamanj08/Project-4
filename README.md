# Project-4

# Project Question: 
Based on the measurements of the key features of the flower (the petal width and length and the sepal width and length) can we accurately classify an Iris Flower by its species?

# Data Source: 
- https://www.kaggle.com/datasets/shantanuss/iris-flower-dataset

# Libraries used: 
- SciKit- Learn
- Python Pandas
 -HTML/CSS
- Flask
- PgAdmin (for the SQL database)
- Tableau
- Joblib

# models we tried: 
- We tried a random forest model with 0.4, 0.3, and 0.2 test sizes, but we decided to go with 0.4 since it yielded 98% accuracy, whereas the others yielded 100% accuracy.
- We also trained and tested a logisitic regression model, which yielded 100% accuracy.  

# model we ended up using and why: 
- We ended up using the random forest model with 0.4 test size. This test size and model yielded 98% accuracy oppososed to 100% accuracy in our other attempts. We decided to use this one because 100% accuracy seemed a bit too accurate.

# visuals we did: 
- We created a bar chart in tableau to visualize the differences in sepal and petal sizes between species.
- We also created a bar chart within jupyter notebook with pandas to visualize the important features. We used the important features to create scatter plots that would show us which species had more similar or more different features.  

# web interface stuff:
- For our web interface, we used HTML/CSS.
- We set up the flask app to connected to our SQL Database that holds all the Iris Flower data.
- Most of the routes in the app were pretty basic besides our Model Predictor tab, which was coded to take user given measurements and provide a predicted Iris Species using our Random Forest model based off of those inputs given.
- We used joblib to connect our machine learning model from our notebook to our app

# references: 
- JobLib usage for the machine learning model: https://maze-runner.medium.com/deploying-the-ml-model-to-the-flask-with-joblib-53f313d24003
