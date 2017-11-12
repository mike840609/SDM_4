# SDM_4

## Virtual Environment
```bash

    $ python3 -m venv  venv

    win:
       $ myvenv\Scripts\activate
    osx :
       $ source myvenv\bin\activate
        
```
## Migrate && Runserver:
```bash
   $ pip install -r requirements.txt

   $ python manage.py makemigrations

   $ python manage.py migrate

   $ python manage.py runserver
```

## Generate the new requirements:
```bash
    pip freeze > requirements.txt
```
