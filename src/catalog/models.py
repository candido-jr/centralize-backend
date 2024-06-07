from django.db import models
from django_extensions.db.models import TimeStampedModel
from mptt.models import MPTTModel, TreeForeignKey
from django.db.models import F


class Category(TimeStampedModel, MPTTModel):
    name = models.CharField(max_length=255)
    parent = TreeForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True, related_name="children"
    )

    class MPTTMeta:
        order_insertion_by = ["name"]

    def __str__(self):
        return self.name


class Product(TimeStampedModel):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(
        Category, related_name="products", on_delete=models.CASCADE
    )
    stock = models.PositiveIntegerField(default=0)
    available = models.BooleanField(default=True)
    image = models.ImageField(upload_to="products/", blank=True, null=True)

    def __str__(self):
        return self.name

    def update_stock(self, quantity):
        if quantity < 0 and abs(quantity) > self.stock:
            raise ValueError("Insufficient stock")
        self.stock = F("stock") + quantity
        self.save()
