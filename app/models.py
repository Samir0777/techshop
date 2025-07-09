from django.db import models

class CardSection(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='card_images/')

    def __str__(self):
        return self.title
