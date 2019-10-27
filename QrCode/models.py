from django.db import models


# Create your models here.
class Gtin(models.Model):
    gtin_number = models.CharField(max_length=30)
    product_name = models.CharField(max_length=30)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name

    class Meta:
        verbose_name_plural = "GTIN NUMBER"
        verbose_name = "GTIN NUMBER"
