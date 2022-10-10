from django.db import models


class Appfile(models.Model):
 tital = models.CharField(max_length=50)
 files = models.FileField(upload_to='uploads')
 
def __str__(self):
     return self.tital