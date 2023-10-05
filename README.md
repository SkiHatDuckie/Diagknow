# Purpose
A healthcare application to determine what disease you may be suffering from depending on symptoms you tell!

# Languages used  
 - HTML/CSS: Website front-end, **index.html**, connecting to the database administration and models, or item types, using the user input.
 - Python: Used in the administration and interface between models and the database of the website, and the catalog of URLs.
 - JavaScript: Used for symptom mapping, disease detection, and graphing of data. 
 - PHP/MySQL: Used to fetch data from the database, and for forming the database as well.  Also used for organization and mapping of data, and most importantly user registration and data input and server management. 
 - CLI (Command line interface): Testing and deploying the system through Django, and for creating the database for the hospital, and inputting data into the database, or for dynamic user data allocation.  Essentially used to interface with the server that hosts the website and to monitor data storage. 
   
# Packages used
 - Django:  Python framework using **client-side tools** and **command-line interface** to create, test and deploy apps in as little time as possible.
 - MySQL:  An open-source database software that uses SQL (Structured query language) to work with your computer's operating system to manage users,  permit network access, facilitates beta testing, creates backups, and implements a relational database in the OS. It generates PHP to the server using the parameters in the database.
 
# Terminals used
 - Command Line Interface: Test and deploy your website through the Django provided files to connect the front-end, the models, the URLs, and the database.

# Website Models (in models.py)
 - User:  Stores the username, password, and personal information of all users.
 - Disease: Users are diagnosed based on which diseases contain the symptoms that they have.
 - Symptom:  What are stored as attributes in the **User** models that will be mapped via MySQL to the different diseases stored in the MySQL database.
 - Hospital: Stores the database of registered users, discovered diseases, and images of symptoms that are inputted into the users' submitted diagnoses.

# Process
❶ **admin.py** will register all models in the website to enable the usage of the models. <br/></br>
❷ **signup.html** asks for a new user's info that will be inputted into the database. <br/></br>
❸ **views.py** processes the newly registered user's information to create instances of the different models in the website. <br/></br>
❹ **process.php** will take the newly inputted user's data, then send a confirmation email to the inputted user's email.  If the user is signing in, it will send a code to the user's inputted phone number as two-factor authentication. <br/></br>
5️ **find.py** will allow the user to input their diagnosis symptoms and any visual evidence, then send it to be mapped to the hospital database. <br/></br>
6️ **search.php** will search through the database for the user's disease based on their symptoms. They will then receive an email back containing their diagnosis and recommended treatments. <br/></br>
