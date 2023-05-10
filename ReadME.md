<h1>Neobis_E-Store_project</h1>

<h3>1. Project description -
the project has implemented the possibility</h3>

+ registration and authorization of users
+ CRUD
+ Rating
+ Review
+ Comments
+ Order

<h1>Installation</h1>

+ Clone the repository using the command

> git@github.com:tturdumamatovv/Neobis_E-Store_project.git

+ Create a virtual environment using the command

> python3 -m venv <name of your environment> 

+ Activate the virtual environment

> source <name of your environment>/bin/activate

+ Install dependencies

> pip install -r requirements.txt 

+ Create .env file

> touch .env

+ Write the data to the .env file
  (env_example)
+ Go to the config directory

> cd config

+ Make migrations

>  ./manage.py migrate

+ Launch your project

> ./manage.py runserver