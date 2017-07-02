from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    name = models.CharField(max_length = 64)
    html = models.TextField()
    css = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)
    class Meta:
        def __str__(self):
            return self.name
