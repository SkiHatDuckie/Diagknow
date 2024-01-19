# Contributing to DiagKnow

This project is currently built using Python v3.10.11.

Before installing django or any other dependencies, create a new virtual environment for django
projects, if one does not already exist.

`python -m venv /path/to/new/virtual/environment/django-env`

For more information on setting up a virtual environment, use this [user guide](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#create-and-use-virtual-environments).

Once the virtual environment is set up, activate it and traverse to the project directory if you
haven't already. Once you've done that, run the following:

`pip install requirements.txt`

This will install all of the necessary dependencies for working on the project.

You can install our Django app by cloning it above or entering:

`git clone https://github.com/oscuml/Diagknow.git'

The website's Django infrastructure is under construction, so you can add modules via the format 
`class Person(models.Model):`
`    SHIRT_SIZES = {`
`        "S": "Small",`
`        "M": "Medium",`
`        "L": "Large",`
`    }`
`    name = models.CharField(max_length=60)`
`    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)`

To make changes, you must log the changes on the migrations.py file, via the format:
`class Migration(migrations.Migration):`
 `   dependencies = [("migrations", "0001_initial")]`

 `   operations = [`
 `       migrations.DeleteModel("Tribble"),`
 `       migrations.AddField("Author", "rating", models.IntegerField(default=0)),`
 `   ]`

To include these migrations, type the command `python manage.py makemigrations` then `python manage.py migrate`.

This will then create a file `0001_initial.py` in our case, which will contain the changes made to the website.

More details can be found here:  https://docs.djangoproject.com/en/5.0/topics/migrations/

Operations that can be done to shortcut modifications to the website are also shown here: https://docs.djangoproject.com/en/4.2/ref/migration-operations/

**This must be done for every change to the website.**
	

# Getting Started with Create React App

This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).

## Available Scripts

In the project directory, you can run:

### `npm start`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in your browser.

The page will reload when you make changes.\
You may also see any lint errors in the console.

### `npm test`

Launches the test runner in the interactive watch mode.\
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

### `npm run build`

Builds the app for production to the `build` folder.\
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.\
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.

### `npm run eject`

**Note: this is a one-way operation. Once you `eject`, you can't go back!**

If you aren't satisfied with the build tool and configuration choices, you can `eject` at any time. This command will remove the single build dependency from your project.

Instead, it will copy all the configuration files and the transitive dependencies (webpack, Babel, ESLint, etc) right into your project so you have full control over them. All of the commands except `eject` will still work, but they will point to the copied scripts so you can tweak them. At this point you're on your own.

You don't have to ever use `eject`. The curated feature set is suitable for small and middle deployments, and you shouldn't feel obligated to use this feature. However we understand that this tool wouldn't be useful if you couldn't customize it when you are ready for it.

## Learn More

You can learn more in the [Create React App documentation](https://facebook.github.io/create-react-app/docs/getting-started).

To learn React, check out the [React documentation](https://reactjs.org/).

### Code Splitting

This section has moved here: [https://facebook.github.io/create-react-app/docs/code-splitting](https://facebook.github.io/create-react-app/docs/code-splitting)

### Analyzing the Bundle Size

This section has moved here: [https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size](https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size)

### Making a Progressive Web App

This section has moved here: [https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app](https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app)

### Advanced Configuration

This section has moved here: [https://facebook.github.io/create-react-app/docs/advanced-configuration](https://facebook.github.io/create-react-app/docs/advanced-configuration)

### Deployment

This section has moved here: [https://facebook.github.io/create-react-app/docs/deployment](https://facebook.github.io/create-react-app/docs/deployment)

### `npm run build` fails to minify

This section has moved here: [https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify](https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify)
