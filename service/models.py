from django.db import models

# Create your models here.
class Service(models.Model):
    ipaddr=models.IPAddressField(unique=True)
    app=models.CharField(max_length=10,null=True)
    application=models.CharField(max_length=50,null=True)
    status=models.IntegerField(default='0')

    def __unicode__(self):
        return self.ipaddr