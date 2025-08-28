### Precautions
- make sure you have `DEBUG = True` in `app.setting.py` while coding and testing

### tailwind
- watch
```
npx tailwindcss -i ./static/css/tailwind.css -o ./static/css/output.css --watch
```

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

---

### Django media
- so many steps to went wrong be cautious
#### 1. Install Pillow

Django uses the Pillow library to handle images.

```bash
pip install Pillow
```



#### 2. Configure Settings (`settings.py`)

Add `MEDIA_URL` and `MEDIA_ROOT` so Django knows where to store uploaded files.

```python
import os

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```



#### 3. Update `urls.py`

Add this in your project’s main `urls.py` to serve media files in development.

```python
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('your_app.urls')),  # replace with your app name
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```


#### 4. Create Model with ImageField

In your `models.py`:

```python
from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True, default='avatars/default.jpg')

    def __str__(self):
        return self.name
```

* `upload_to='avatars/'` → images will be saved under `media/avatars/`.
* `blank=True, null=True` → allows no image.
* `default` → provides a fallback image.



#### 5. Create & Run Migration

```bash
python manage.py makemigrations
python manage.py migrate
```



#### 6. Create Form

In `forms.py`:

```python
from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'avatar']
```



#### 7. Update View

In `views.py`:

```python
from django.shortcuts import render, redirect
from .forms import ProfileForm

def create_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('profile_list')  # change to your redirect view
    else:
        form = ProfileForm()
    return render(request, 'create_profile.html', {'form': form})
```

⚡ Note: Use `request.FILES` for file uploads.



#### 8. Create Template

In `create_profile.html`:

```html
<form method="post" enctype="multipart/form-data">
  {% csrf_token %}
  {{ form.as_p }}
  <button type="submit">Upload</button>
</form>
```

* `enctype="multipart/form-data"` is required for file uploads.



#### 9. Display Uploaded Images

In a template:

```html
{% for profile in profiles %}
  <p>{{ profile.name }}</p>
  {% if profile.avatar %}
    <img src="{{ profile.avatar.url }}" alt="{{ profile.name }}" width="150">
  {% endif %}
{% endfor %}
```


