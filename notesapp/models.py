from django.db import models

# Create your models here.
class notestable(models.Model):
    ntitle=models.CharField(max_length=20)
    ndesc=models.TextField(max_length=1000)
    nstatus=models.BooleanField(default=False)
    class Meta:
        db_table='notestable'
    def __str__(self):
         return self.ntitle
