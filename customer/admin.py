from django.contrib import admin
from .models import Details

# Register your models here.
class DetailsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'password',)

admin.site.register(Details, DetailsAdmin)