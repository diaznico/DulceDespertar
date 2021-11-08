from django.contrib import admin
from .models import adicionales

# Register your models here.

class adicional_admin(admin.ModelAdmin):
    readonly_fields=('created','update')

admin.site.register(adicionales, adicional_admin)
