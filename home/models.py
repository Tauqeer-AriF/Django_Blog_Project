from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=150)
    desc = models.TextField()
    blog_image = models.ImageField(upload_to="img/%y")


class Contact(models.Model):
    fname = models.CharField(max_length=122)
    lname = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=122)
    message = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.fname