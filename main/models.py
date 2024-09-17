import uuid
from django.db import models

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # tambahkan baris ini
    name = models.CharField(max_length=255)  # Nama produk
    price = models.IntegerField()  # Harga produk
    feedback = models.TextField()  # Feedback produk
    rating = models.IntegerField(default=0)  # Rating produk

    def __str__(self):
        return self.name
