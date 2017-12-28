TeamManagement
======================================================

:Author: Gaurav Kumar <aavrug@gmail.com>

TeamManagement is for managing teams.

We need virtualenv if that is in your system then ok or for installation follow the link https://virtualenv.pypa.io/en/stable/installation/

Steps for Setup
======================================================

    git clone https://github.com/aavrug/TeamManagement.git

    cd TeamManagement

    git checkout develop

    virtualenv venv

    source venv/bin/activate

    pip install -r requirements.txt

    cd TeamManagementProject

Database Setup
======================================================

Create a new database TeamManagement and change MySQL credentials as per your configuration in "settings.py".

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'TeamManagement',
            'USER': 'Your MySQL Username',
            'PASSWORD': 'Your MySQL Password',
            'HOST': 'localhost',
            'PORT': '',
        }
    }


From TeamManagementProject directory run the command

    python manage.py migrate

    python manage.py runserver

Testing with methods
======================================================

After starting the server you can open 127.0.0.1:8000 in your browser, also you can test the methods from terminal.

By default the port number will be 8000 but If that is in use you can change it with the following command.

    python manage.py runserver 127.0.0.1:8080

Open a new tab in the terminal and use the following CURL commands for Create, List, Update and Delete.

The given data for the columns is just an example, you can pass your own data and test.

List
======================================================

    curl -X GET -H "Content-Type:application/json" http://127.0.0.1:8000/teamlists/

Create
======================================================

    curl -X POST -H "Content-Type:application/json" http://127.0.0.1:8000/teamlists/ -d '{"first_name": "David", "last_name": "Jones", "phone": "1510123456", "email": "test@test.com", "role": 0}'

Update
======================================================

    curl -X PATCH -H "Content-Type:application/json" http://127.0.0.1:8000/teamlists/1/ -d '{"first_name": "James"}'

Delete
======================================================

    curl -X DELETE -H "Content-Type:application/json" http://127.0.0.1:8000/teamlists/1/

