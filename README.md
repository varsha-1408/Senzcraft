# Senzcraft
## **WHAT IS THIS?**
This application is used to extract pre-defined fields from a standard JSON file and save the same to a DB using the technology like python, Mysql.

## **COMMANDS**-

# **To install django and its frameowork**-

pip install django

python manage.py makemigrations

python manage.py migrate

pip install django-rest-framework

# **To connect python and mysql**-

pip install mysqlclient

pip install mysql-connector-python

## **WORKING OF FILES**-

manage.py- It is automatically created in each Django file.All the configuations are loaded inside this file.

settings.py- This file is inside the manage.py file. We have added our senzcraft app in this file and added the configuration of the database.

senzcraft- Its an application for our project.

models.py- Its a file inside senzcraft. Models are basically tables. Here aor table name is ConfidenceScore and we have three rows in it like text, confidence, bounding_box.

serializer.py-Serializers allow complex data such as querysets and model instances to be converted to native Python datatypes that can then be easily rendered into JSON , XML or other content types.
Two serializers are made -ConfidenceScoreListSerializer and ConfidenceScoreSerializer.

views.py-Its a file inside serializer. In this file we have two http request- post_confidence_score and get_confidence_score.

senzcraft/urls.py-I have define the urls inside this file.

varshaproject/urls.py-I have defined the path for the urls defined in the senzcraft/urls.py.


