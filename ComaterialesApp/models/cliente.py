from django.db import models

class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=50, null=False)
    gender = models.CharField(max_length=10)
    age = models.CharField(max_length=3)
    phone = models.CharField(max_length=15, null=False)
    address = models.CharField(max_length=100,null=False)
    email = models.EmailField(max_length=100, null=False)
    city_code = models.CharField(max_length=10, null=False)
    country_code = models.CharField(max_length=10, null=False)
    created_at = models.TimeField()
    password = models.CharField(max_length=20)
