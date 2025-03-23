from django.db import models
from sorl.thumbnail import ImageField # type: ignore

class Post(models.Model):
    text = models.CharField(max_length=150, blank=False, null=False)
    image = ImageField()

    def __str__(self):
        return self.text
