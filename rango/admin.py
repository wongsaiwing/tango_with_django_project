from django.contrib import admin
from rango.models import Category, Page

class Cust_Admin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')

admin.site.register(Category)
admin.site.register(Page, Cust_Admin)

# Register your models here.