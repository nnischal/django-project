from django.db import models

# Create your models here.
class Students(models.Model):
    name = models.CharField(max_length=150)
    age = models.IntegerField()
    address = models.CharField(max_length=300)

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"


    