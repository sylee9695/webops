from django.db import models

# Create your models here.

class Ip(models.Model):
    ipaddr=models.IPAddressField(unique=True)
    hostname=models.CharField(max_length=50,null=True)
    ostype=models.CharField(max_length=20)
    ports=models.CharField(max_length=10,null=True)
    application=models.CharField(max_length=50,null=True)
    status=models.IntegerField(default='1')

    def __unicode__(self):
        return self.ipaddr

class Device(models.Model):
    ipaddr=models.IPAddressField(unique=True)
    cpu=models.CharField(max_length=20)
    memory=models.CharField(max_length=20)
    location=models.CharField(max_length=20)
    product=models.CharField(max_length=20)
    platform=models.CharField(max_length=20,null=True)
    sn=models.CharField(max_length=20)



    def __unicode__(self):
        return self.ipaddr
