from django.db import models

# Create your models here.
class User(models.Model):
    uid = models.AutoField(primary_key=True)
    uname = models.CharField(max_length=32)
    psw = models.CharField(max_length=64)
    def toDict(self):
        return {'uid':self.uid, 'name':self.uname, 'password':self.psw}

class shop_list(models.Model):
    sid = models.AutoField(primary_key=True)
    sname = models.CharField(max_length=32)
    xinx = models.CharField(max_length=32)
    star_time = models.DateField()
    stop_time = models.DateField()
    price = models.DecimalField(max_digits=5,decimal_places=2)



