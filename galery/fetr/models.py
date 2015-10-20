from django.db import models

# Create your models here.
class Album(models.Model):
    name=models.CharField(max_length=100)
    album_picture=models.ImageField(upload_to="images")

    def __unicode__(self):
        return self.name

class Image(models.Model):
    image=models.ImageField(upload_to="images")
    image_name=models.CharField(max_length=100)
    album=models.ForeignKey(Album)

    def __unicode__(self):
        return self.image_name
