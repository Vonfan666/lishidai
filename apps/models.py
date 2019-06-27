from django.db import models

# Create your models here.


class Login(models.Model):

    id=models.IntegerField(primary_key=True,unique=True)
    phone=models.CharField(max_length=11)
    pwd=models.CharField(max_length=18)
    createtime=models.DateTimeField(auto_now_add=True)
    # updatetime=models.DateTimeField(auto_now_add=True)
    class Meta():
        db_table='login'

    def __str__(self):
        return self.phone
