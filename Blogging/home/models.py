from django.db import models

# Create your models here.

class contact1(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=13)
    content= models.TextField()
    email= models.CharField(max_length=100)
    timestamp=models.DateTimeField(auto_now_add=True,blank=True)


    def __str__(self):
        return 'Message from '+ self.name +"-----"+ self.email


