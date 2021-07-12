from django.db import models


class Post(models.Model):
    text = models.TextField()  # Declares a column in the db called "text" of type TextField

    def __str__(self):
        return self.text[:50]