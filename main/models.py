from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)  # Nama produk
    price = models.IntegerField()  # Harga produk
    description = models.TextField()  # Deskripsi produk
    size = models.CharField(max_length=50)  # Ukuran produk (misalnya S, M, L)

    def __str__(self):
        return self.name
