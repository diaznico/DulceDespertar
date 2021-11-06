from django.contrib import admin
from django.contrib.admin.filters import RelatedOnlyFieldListFilter
from .models import desayunos

# Register your models here.

class desayunos_admin(admin.ModelAdmin):
    readonly_fields=('created','update')

admin.site.register(desayunos, desayunos_admin)
