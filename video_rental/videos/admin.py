from django.contrib import admin
from . import models


# Register your models here.

class MovieAdmin(admin.ModelAdmin):
    # order of the fields when showed in detail view inside admin site
    fields = ['release_year', 'title', 'length']


admin.site.register(models.Customer)
admin.site.register(models.Movie, MovieAdmin)
