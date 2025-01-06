# vue-drf-interface
Vue 3 Interface to Django REST Framework
## About 
Simple single-page Vue front end application that reads specified REST endpoint and provides tabular editable sortable interface to exposed endpoints
### Front End
The Vue 3 application does the following:

 - reads root endpoint and find all exposed endpoints
 - routs endpoints as pages in application
 - GETs particular endpoint and tabularizes the data based on OPTIONS
 - provides ability to add and edit objects based on OPTIONS 
 - validates data both client-side and server side
 - paginates the results
 - provides editing to 'choices' fields and foreign key search select fields
to run see [README](vue-front-end/README.md)
### Back End
Django Rest Framework with PostgreSQL : 

 - Provides REST API
 - So far only two serialized models
 
   - Customer
   - Queue (with foreign key to Customer)


to run see [README](django-docker/README.md)

![alt text](screenshots/main.png)
