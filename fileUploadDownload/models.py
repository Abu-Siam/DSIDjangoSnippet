import os

from django.db import models

# Create your models here.
class FileDetailsModel(models.Model):
    name = models.CharField(max_length=100)
    owner = models.CharField(max_length=100,unique=True)
    pdf = models.FileField(upload_to='storage/pdf/')
    cover = models.ImageField(upload_to='storage/image/')



    def __str__(self):
        return self.name

class FileTempStorage(models.Model):
    pdf = models.FileField(upload_to='storage/temp/')
    def __str__(self):
        return os.path.basename(self.pdf.name)