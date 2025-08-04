### create app
```
python .\manage.py startapp core
```
- here `core` is the app_name
- we store cummon things in the core

### Adding global static
- therer are so many places to make mistakes
- editing setting. `STATICFILES_DIRS` spelling 
```
STATIC_URL = 'static/' 
STATICFILES_DIRS = [
    BASE_DIR / "static"
]
```
- inside html place load static at the top
```python
{% load static %}
```
- then can use the variable as following `{% static 'css/style.css' %}`
```
<link rel='stylesheet' type='text/css' href="{% static 'css/style.css' %}">
```

### Setup postgress
- setup `settings.py`
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'task_manager',
        'USER': 'postgres',
        'PASSWORD': '123456',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}
```
- set the db name in `NAME` field
- install plugins
```
pip install psycopg-binary
pip install psycopg
```
- migrate data base
```
python manage.py migrate  
```

### make Model
- declear modele in `app/models.py`
- create a py file that will create tables / make-migrations
```bash
python .\manage.py makemigrations
```
- create actual table in db
```bash
python .\manage.py migrate
```

### django admin
- create admin 
```
python .\manage.py createsuperuser
```
- every model must have `__str__` method defined to be able to edit from django admin page