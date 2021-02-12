from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

admin.site.register(Mode)
admin.site.register(Catalogue)
admin.site.register(CatalogueMetadata)
admin.site.register(Item)
admin.site.register(ItemMetadata)
