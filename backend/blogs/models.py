from django.db import models
from django.contrib.auth.models import User

class UsersPosts(models.Model):
    is_published = models.BooleanField(default=False)
    is_delete = models.BooleanField(default=False)
    author = models.ForeignKey(User , on_delete=models.CASCADE)
    publish_date = models.DateField(auto_now=True)
    title = models.CharField(max_length=200)
    main_text = models.TextField()
