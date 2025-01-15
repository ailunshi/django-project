from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE) # on_delete tells Django what to do with post if user of this post is deleted
    
    def __str__(self):
        return self.title
    
"""
user = User.objects.filter(username='ailunshi').first()
all the posts that a user has created: user.post_set
run queries: user.post_set.all()
create post: user.post_set.create(title='Blog 3', content='Third Post Content')
"""