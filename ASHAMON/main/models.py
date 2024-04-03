from django.db import models

# Create your models here.
#When models are updated, we must save this file and then tell Django we have updated
#our models by running the command: python manage.py makemigrations main
#This will stage your changes to the models.
#After the migrations are made or "staged," we then run the following command to apply them:
#Python c:/Users/pbark005/source/vscode/ASHAMON_Dj/ASHAMON/manage.py migrate
#The changes are then migrated into the django app and the changes are saved under the migrations folder as ####_Initial.py
#These initial.py files can be used to revert to previous states if an error is introduced to the app
### New Comment
class ToDoList(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class Item(models.Model):
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    complete = models.BooleanField()

    def __str__(self):
        return self.text
