from django.contrib import admin

from .models import Classification, Object, Document

admin.site.register(Classification)
admin.site.register(Object)
admin.site.register(Document)
