from django.db import models

# Create your models here.
class Food(models.Model):
    name = models.CharField(max_length=20)

    def __unicode__(self):
        return self.name