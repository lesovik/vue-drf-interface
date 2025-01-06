# django-docker

## Project setup
```
docker-compose up --build
```

### Create database
```
docker-compose run web python3 manage.py makemigrations
docker-compose run web python3 manage.py migrate
docker-compose run web python3 manage.py createsuperuser
```


