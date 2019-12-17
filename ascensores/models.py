from django.db import models
from django.urls import reverse
import uuid

# Create your models here.

class SolicitudEmpresa(models.Model):
    nombreEmp=models.CharField(max_length=30, primary_key=True)
    email=models.EmailField(max_length=60)
    direccion=models.CharField(max_length=200)
    class Meta:
        ordering =['nombreEmp']
    
    
    def get_absolute_url(self):
        return reverse('solicitudempresa-detail',args=[str(self.nombreEmp)])

    def __str__(self):
        return f'{self.nombreEmp},{self.email},{self.direccion}'