# Forex Converter!

## With using just python, flask and the forex-python with the MicroPyramid API

There is four aspects to this project.

1. Using the flask package to create a server to hold the main page as well as handle the post request from the user.
2. The helper file which imports the forex_python package and retreives the currency code and currency amount and converts it into a dollar amount with two decimals.
3. The base.html file that holds the main skeleton of the form which has bootstrap also included. I did not include a .css file and let bootstrap do all the lifting with styling. Kept it simple.
4. Lastly the two test files tested the functionality of both the routes created in the app.py file and the calculation file within the helper.py file.
