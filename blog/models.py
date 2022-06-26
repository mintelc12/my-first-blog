from django.conf import settings
from django.db import models
from django.utils import timezone

<<<<<<< HEAD
=======

>>>>>>> cf86ce2f097b3bf8c1da68e9454f8fcdc7297b36
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
<<<<<<< HEAD
        return self.title
=======
        return self.title
>>>>>>> cf86ce2f097b3bf8c1da68e9454f8fcdc7297b36
