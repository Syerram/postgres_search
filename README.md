# Postgres Search in Django

This project attempts to do couple of things
1. Postgres Full text search
2. Django integration with Postgres Search using South
3. Celery task to asyncronously update the Search table
4. AngularJS for front end coding

## Install

* Create a database in Postgres, note down the user, password, database and schema name. 
  * Make sure you set the `search_path` to the `schema` name on the user.
* Download the code
* From the root, run `bin/install.sh data/Users.xml`. It will try to load the stackexchange DBA users
* On a separate terminal run `bin/celery.sh`
* Then run the server `bin/run.sh runserver --noreload 0.0.0.0:8080`
* Goto `http://localhost:8080` and test the search

Explore comments and keep checking as I add more code to it, e.g. Ranking, Similarity

## Haystack
* I am planning to add postgres search to haystack so its available for users using Haystack
