from django.contrib import admin
from . import models


# Register your models here.

class MovieAdmin(admin.ModelAdmin):
    # order of the fields when showed in detail view inside admin site
    fields = ['release_year', 'title', 'length']
    # django will create a search box for title
    search_fields = ['title']
    # django will create a filter box for the fields listed
    list_filter = ['release_year', 'length']
    # admin list view will show all the attributed listed here
    list_display = ['title', 'release_year', 'length']
    # what you can edit from the list view
    list_editable = ['length']


admin.site.register(models.Customer)
admin.site.register(models.Movie, MovieAdmin)
