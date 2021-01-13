from django.db import models


class Catalogue(models.Model):
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return "Catalogue"


class Mode(models.Model):
    id = models.CharField(primary_key=True, max_length=10)
    short_desc = models.CharField(max_length=50)
    long_desc = models.TextField(null=True)

    def __str__(self):
        return self.short_desc


class CatalogueMetadata(models.Model):
    catalogue = models.ForeignKey(Catalogue, on_delete=models.CASCADE, related_name="catalogue_metadata", null=True)
    rel = models.TextField(null=True)
    val = models.TextField(null=True)

    def __str__(self):
        return self.val


class Item(models.Model):
    href = models.URLField()
    catalogue = models.ForeignKey(Catalogue, on_delete=models.CASCADE, related_name="item", null=True)

    def __str__(self):
        return self.href


class ItemMetadata(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="item_metadata", null=True)
    rel = models.TextField(null=True)
    val = models.TextField(null=True)

    def __str__(self):
        return self.val
