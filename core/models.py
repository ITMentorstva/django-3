from django.db import models

# class Product -> tabela product u DB

class Product(models.Model):
    title = models.CharField(max_length=200) # title, VARCHAR(200)
    price = models.DecimalField(max_digits=10, decimal_places=2) # 5555.22
    description = models.TextField(blank=True) # description, TEXT, NULL

    class Meta:
        db_table = 'product'