from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) #on delete: what to do if user is deleted, if user is deleted, delete the profile; if profile is deleted, user will not be deleted
    # can add other stuff, like bio, current city
    image = models.ImageField(default="default.jpg", upload_to="profile_pics") # upload_to: directory where images get uploaded to

# dunder str method, otherwise printing out a profile will result in profile object
    def __str__(self):
        return f"{self.user.username} Profile"
    
# whenever a change is made to the model, a change is made to the database, so run migrations