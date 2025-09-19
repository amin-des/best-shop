from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class UsersPosts(models.Model):
    is_published = models.BooleanField(default=False)
    is_delete = models.BooleanField(default=False)
    author = models.ForeignKey(User , on_delete=models.CASCADE)
    publish_date = models.DateField(auto_now=True)
    title = models.CharField(max_length=200)
    main_text = models.TextField()
