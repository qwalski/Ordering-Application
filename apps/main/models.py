from django.contrib.auth.models import User
from django.db import models


class Items(models.Model):
    """
        Item entity that list the details of a particular item
    """
    item_name = models.CharField(max_length=100)
    picture = models.ImageField(upload_to="inventory/", max_length=100)
    item_price = models.IntegerField(default=0)

    class Meta:
        app_label = "main"
        verbose_name_plural = "Items"

    def __str__(self):
        return self.item_name


class Orders(models.Model):
    """
        Orders relationship with user and item as foreign key
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey("Items", on_delete=models.CASCADE)
    order_count = models.IntegerField(default=1)

    class Meta:
        app_label = "main"
        verbose_name_plural = "Orders"

    def __str__(self):
        return "{} {}".format(self.user, self.item)


class Inventory(models.Model):
    """
        Inventory entity that contains the list of all items
    """    
    item  = models.ForeignKey("Items", on_delete=models.CASCADE)
    item_count = models.IntegerField(default=0)

    class Meta:
        app_label = "main"
        verbose_name_plural = "Inventories"

    def __str__(self):
        return "{} {}".format(self.item, self.item_count)
