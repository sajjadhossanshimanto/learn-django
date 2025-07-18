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