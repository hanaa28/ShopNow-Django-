from django.db import models

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    # image = models.ImageField(upload_to='product_images/')
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    add_date = models.DateTimeField(auto_now_add=True)  # Automatically set when object is first created
    update_date = models.DateTimeField(auto_now=True)   # Automatically set every time object is updated
