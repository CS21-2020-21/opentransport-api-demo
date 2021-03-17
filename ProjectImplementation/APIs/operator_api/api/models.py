from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    operator_id = models.CharField(max_length=10, null=True, unique=True)


def save(self, *args, **kwargs):
    super().save(*args, **kwargs)


def userprofile_receiver(sender, instance, created, *args, **kwargs):
    if created:
        userprofile = UserProfile.objects.create(user=instance)
    else:
        instance.userprofile.save()


post_save.connect(userprofile_receiver, sender=User)


class Catalogue(models.Model):
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return 'Catalogue'


class Mode(models.Model):
    id = models.CharField(primary_key=True, max_length=10)
    short_desc = models.CharField(max_length=50)
    long_desc = models.TextField(null=True)

    def __str__(self):
        return self.short_desc


class CatalogueMetadata(models.Model):
    catalogue = models.ForeignKey(Catalogue, on_delete=models.CASCADE, related_name='catalogue_metadata', null=True)
    rel = models.TextField(null=True)
    val = models.TextField(null=True)

    def __str__(self):
        return self.val


class Item(models.Model):
    operator_id = models.CharField(max_length=10, null=True, unique=True)
    href = models.URLField()
    catalogue = models.ForeignKey(Catalogue, on_delete=models.CASCADE, related_name='item', null=True)

    def __str__(self):
        return self.href


class ItemMetadata(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='item_metadata', null=True)
    rel = models.TextField(null=True)
    val = models.TextField(null=True)

    def __str__(self):
        return self.val
