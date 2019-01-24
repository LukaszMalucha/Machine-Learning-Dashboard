# ML Dashboard Project

[Visit App on Heroku](https://mldashboardproject.herokuapp.com/)



## Project Case:

ML Dashboard – a place where developers can store, edit and share code templates. 
ML Dashboard – also a place where starting programmers can download fully-described 
machine learning algorithm in order to include it in their own project or even see it in action once implemented on the use case.



## Project Requirements:
1.	Create a web application that allows users to store and easily access machine learning templates.
2.	Build relational database to store them.
2.	Create the backend code and frontend form to allow users to add new templates to the site.
3.	Create the backend code to group and summarises the templates on the site, based on their attributes (type of algorithm).
4.	Matplotlib visualisations.
5.	CRUD operations can be carried out using either SQL (e.g. MySQL/SQLite/Postgres) or NoSQL (e.g. MongoDB). 
6.	Use Flask micor-framework.
7.	Create the backend code to retrieve a list of recipes.
8.	Basic user registration and authentication to the site.
9.	Make sure your site is as responsive as possible.
10.	Logic must be written in Python. HTML, CSS, and JavaScript can be used to enhance the look and feel of the dashboard.
11.	The website must be data-driven and can rely on structured data, unstructured data or a mix of structured and unstructured data.


## Tools, Modules and Techniques:

##### Python – web development:
flask | wtforms | werkzeug
##### Python – DB:
flask_sqlalchemy
##### Python – data analysis & visualisation:
pandas | numpy | matplotlib | seaborn
##### Python – machine learning:
sklearn | scipy
##### Database Development:
SQLite
##### Web Development:
HTML | CSS | Bootstrap | Materialize | JavaScript | JQuery


## Database Structure:
![db_diagram](https://user-images.githubusercontent.com/26208598/38703823-39169bd2-3e9c-11e8-80a2-d90df2c9274b.JPG)
Database structure can be divided into 3 main parts:
##### User Credentials:
Stored in a one table, password additionally secured with SHA-256 
##### ML Dashboard View:
Database tables that are building blocks for a data-table displayed on a main page. 
Additionally those tables are guaranteeing add/edit function integrity. Relationship type: one-to-one
##### ML Algorithm Type Information:
Three separate tables with many-to-many relationship compiled within “Assembler Table”.


## App Structure:

### Main Dashboard:
![dashboard](https://user-images.githubusercontent.com/26208598/38704139-52ce30ca-3e9d-11e8-9613-a2da6001c4d9.JPG)


Main page on an application. Built with three main components:

##### DataTable
Contains all available code templates. Main features are:
1. Contribute – redirect to “add template” page
2. Records per page button – allows to scale table view (10- 100)
3. Search – datatable keyword search 
4. Clickable headers - datatable sorting functionality
5. “Type of Estimator” button – redirects to type summary
6. “Edit” button – redirect to “edit template”
7. “Delete” button – removes code template from database
8. “Download” button – downloads the code template in a *.py form
9. “Downloads” – downloads counter
10. Previous/Next - pagination feature

##### Types of Estimator
Each button redirects to type summary page

##### Check other projects
Github Repository View, defaulting to my own repo, with an option to change to another contributor.

### Add template:
![add](https://user-images.githubusercontent.com/26208598/38704166-61f8d06e-3e9d-11e8-8f25-00463d2ea312.JPG)
Page contains form that allows user to upload template. 
Built with Materialize accordion, requires all fields to be filled. Accepts only .py files format.

### Edit template:
![edit](https://user-images.githubusercontent.com/26208598/38704186-6c561134-3e9d-11e8-9549-27cf48169641.JPG)
Page contains form that allows user to edit existing template.

### Summary Classification/Regression/Clustering
![sum1](https://user-images.githubusercontent.com/26208598/38704204-7bb7f066-3e9d-11e8-8fa2-4d9071823853.JPG)

Pages that allows user to get an idea about each time and how to differ between them.
At the top of the page there is a high overview about each of the algorithm types. “Preprocessing” & “Possible Issues” are supplied by database (many-to-many relationship).

“ML Regression in action” part starts with a business case, which answers question “Why?”
We can also see dataset characteristics – size, stats & first 10 rows. Those information will allow user to answer question “What?”


All of the above is getting summarized by formulated “Data Question” and then we are ready for some “live” machine learning action.
First column allows user to choose from one of three available algorithms. Once backend finishes analyzing dataset, results and plots are being deployed in remaining columns.  
![sum2](https://user-images.githubusercontent.com/26208598/38704223-8b2ac582-3e9d-11e8-9575-b1280a328861.JPG)


### Sign In/ Log In
![log](https://user-images.githubusercontent.com/26208598/38704298-c4b9f688-3e9d-11e8-8435-c9effa1ae132.JPG)
Top right corner dropdown menu gives user basic sign in/login functionality. 
Available credentials:
User: Test
Password: testtest

## Test Suite:

### Travis CI:

[![Build Status](https://travis-ci.com/LukaszMalucha/Machine-Learning-Dashboard.svg?branch=master)](https://travis-ci.com/LukaszMalucha/Machine-Learning-Dashboard)

### Test Files:

##### test.py

### Manual Tests:

#### Login/Signin Form Test:
1. Is data properly saved in database
2. Are different templates properly routing to signup and login urls
3. Are form fields values properly validated (example: email field)
4. Is password properly hashed in a signup file

#### Main Dashboard:
1. Is database populating tables/columns correctly
2. Button functionality (edit/delete/download/routing)
3. Datatable features working properly (pagination/scaling/headers)
4. Github repo projects displaying properly. Repos searchability


#### Add template/Edit template
1. Fields properly connected to the database
2. Forms are populating database correctly
3. Accepted input file
4. Missing Input test

 
#### Summary Classification/Regression/Clustering
1. Algotypes database populating fields properly
2. Pandas dataframe gives correct information about dataset
3. "Choose algorithm" displays proper options
4. Plot visualisation correct
5. Algorithm results correct

#### App Responsivity: 
1. Done with Inspect element tool as a last part of the test suite


## CREDITS & INSPIRATIONS

#### Error 404 template:

Robin Selmer:

https://codepen.io/robinselmer/pen/vJjbOZ



Enjoy,

Lukasz Malucha