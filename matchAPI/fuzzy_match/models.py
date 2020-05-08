from django.db import models


# Shopify data model
class Shopify_db(models.Model):
    SP_item_id = models.IntegerField(unique=True)
    SP_shop_name = models.CharField(max_length=100)
    SP_item_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return '{} {} {}'.format(self.SP_item_id, self.SP_item_name, self.SP_shop_name)


# TasteGuru data model
class Tasteguru_db(models.Model):
    TG_item_id = models.IntegerField(unique=True)
    TG_item_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return '{} {}'.format(self.TG_item_id, self.TG_item_name)


# Bridge table
class SP_TS_Bridge(models.Model):
    SP_item_name = models.ForeignKey(Shopify_db, on_delete=models.CASCADE)
    TG_item_name = models.ForeignKey(Tasteguru_db, on_delete=models.CASCADE)

    def __str__(self):
        return '{} {}'.format(self.SP_item_name, self.TG_item_name)
