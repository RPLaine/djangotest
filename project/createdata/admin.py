from django.contrib import admin
from .models import SimpleData, OptionalData

admin.site.register(SimpleData)
admin.site.register(OptionalData)