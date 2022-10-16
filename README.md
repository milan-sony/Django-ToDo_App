# django-todoapp

This is a simple todo application build with django

## Features

- Simple UI
- Responsive design
- Multi-user login
- CRUD functionalities for todolists
- Status update for todolists (pending/completed)
- Todo list data is encrypted using [django-cryptography](https://github.com/georgemarshall/django-cryptography)

## Run Locally

You will need to install Python on  you system. Head over to https://www.python.org/downloads/ to download python.
(Dont Forget to Tick Add to Path while installing Python)

Once you have downloaded Python on your system, 
run the following command inside your terminal

```bash
  git clone https://github.com/milan-sony/django-todoapp.git
```

Then go to the project folder

```bash
  cd django-todoapp
```

(This is optional, but strongly recommended) Make a virtual environment

```bash
  python -m venv venv
```

Activate the virtual environment

```bash
  venv/Scripts/activate
```

If error occurs when activating virtual environment, run the following command

```bash
  Set-ExecutionPolicy Unrestricted
```

Install the dependencies needed for this project

```bash
  pip install -r requirement.txt
```

Now minimize the terminal and make a database on MySQL named `django_todoapp`

Once you have created the database, open the project folder inside a code editor (if you don't have a code editor install one). Then open the file named `.env.example` and do as per mentioned  on that file

After creating the `.env` file, head back to the terminal and make migrations

```bash
  python manage.py makemigrations
```

This will create all the migration files (database migrations) required to run this project

Now apply this migrations

```bash
  python manage.py migrate
```

Then run the server

```bash
  python manage.py runserver
```

Once the server is hosted click on the link http://127.0.0.1:8000/
