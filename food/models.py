from django.db import models


# Create your models here.
class Item(models.Model):
    def __str__(self):
        return self.item_name

    item_name = models.CharField(max_length=200)
    item_description = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_image = models.CharField(
        max_length=500,
        default="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT6-g6RtuMHoRdlcBwoNSO-TENKF_GBxzZntIQ_BJD2&s",
    )
