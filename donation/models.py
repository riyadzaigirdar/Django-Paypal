from django.db import models

class Donation(models.Model):
    name = models.CharField(max_length=50)
    amount = models.FloatField()
    is_donated = models.BooleanField(default=False)

    def __str__(self):
        return self.name 
