from django.db import models
from datetime import datetime
from django.utils import timezone
from django.conf import settings
# Create your models here.



class Post(models.Model):
    
    """Model with name getting from loged in user, title of the post displayed as identifier, text of post, created at data which is taken at creation time automatically and published at date, which is taken when publish method is called. """
    
    name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField('Title of post',max_length=125)
    text = models.TextField('Enter the text here')
    created_at = models.DateTimeField(default=timezone.now)
    published_at = models.DateTimeField(null=True, blank=True)
    
    def publish(self):
        self.published_at = timezone.now()
        self.save()
    
    def __str__(self):
        return self.title