# whenever a change is made to the model, a change is made to the database, so run migrations

from django.db import models
from django.contrib.auth.models import User
#from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) #on delete: what to do if user is deleted, if user is deleted, delete the profile; if profile is deleted, user will not be deleted
    # can add other stuff, like bio, current city
    image = models.ImageField(default="default.jpg", upload_to="profile_pics") # upload_to: directory where images get uploaded to
    
# dunder str method, otherwise printing out a profile will result in profile object
    def __str__(self):
        return f"{self.user.username} Profile"
    

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs) # run save method of parent class

    #     img = Image.open(self.image.path)

    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)

    #     #can also delete old files when new ones are uploaded

        


