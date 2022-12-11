from django.contrib import admin
from phones.models import Phone
# Register your models here.

class PhoneAdmin(admin.ModelAdmin):
    repopulated_fields = {"slug": ("name",)}


admin.site.register(Phone, PhoneAdmin)
