from django.db import models


# Create your models here.
class createDBPost(models.Model):
    title=models.CharField(max_length=255)
    text=models.CharField(max_length=255)
    category=models.CharField(max_length=255)
    order=models.CharField(max_length=255,default='')
    image=models.FileField(upload_to='', blank=True)

    def __str__(self):
        return self.title +self.image
