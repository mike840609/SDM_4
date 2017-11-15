# SDM_4

## Virtual Environment
```bash

    $ python3 -m venv  venv

    win:
       $ venv\Scripts\activate
    osx :
       $ source venv\bin\activate
        
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


## Run on NTU　Server:
```bash
    python manage.py runserver 0.0.00:8000
```

https://140.112.107.237:8000