from django.db import models
from django.contrib.auth.models import User

# represent todo model
class Todo(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField(max_length=100, blank=True) # blank is equal to null
    created = models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField(null=True, blank=True) # null is blank for DateTimeField
    important = models.BooleanField(default=False)
    # onhold = models.BooleanField(default=False)
    user =  models.ForeignKey(User, on_delete=models.CASCADE) # foreign key/relationship 

    # display the todos better in admin

    def __str__(self):
        return self.title

