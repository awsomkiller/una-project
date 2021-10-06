from django.db import models

# Create your models here.
class product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    img = models.ImageField(upload_to="imagecontainer/media")
    desc = models.CharField(max_length=100)