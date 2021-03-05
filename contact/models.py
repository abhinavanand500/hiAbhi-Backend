from django.db import models

# Create your models here.
class Contact(models.Model):
    sno = models.AutoField(primary_key = True)
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    query = models.CharField(max_length=700)

    def __str__(self):
        return self.name