from django.conf import settings
from django.db import models
from django.utils import timezone

class Book(models.Model):
    name = models.CharField(max_length=25)
    author = models.CharField(max_length=30)
    store = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='book_images/', null=True)

    def __str__(self):
        return self.name
