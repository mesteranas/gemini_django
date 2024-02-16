from django.db import models

# Create your models here.
class IMGModel(models.Model):
    IMG=models.ImageField(upload_to="images/")