from rest_framework import serializers

from .models import *


class ModeSerializer(serializers.ModelSerializer):
    class Meta:
        ordering = ['id']
        model = Mode
        fields = ('id', 'short_desc', 'long_desc')


class CatMetadataSerializer(serializers.ModelSerializer):
    class Meta:
        ordering = ['id']
        model = CatalogueMetadata
        fields = ('rel', 'val')


class ItemMetadataSerializer(serializers.ModelSerializer):
    class Meta:
        ordering = ['id']
        model = ItemMetadata
        fields = ('rel', 'val')


class ItemSerializer(serializers.ModelSerializer):
    item_metadata = ItemMetadataSerializer(many=True, read_only=True)

    class Meta:
        ordering = ['id']
        model = Item
        fields = ('href', 'item_metadata')


class CatalogueSerializer(serializers.ModelSerializer):
    item = ItemSerializer(many=True, read_only=True)
    catalogue_metadata = CatMetadataSerializer(many=True, read_only=True)

    class Meta:
        ordering = ['id']
        model = Catalogue
        fields = ('catalogue_metadata', 'item')
