from django.contrib import admin
from . models import Category,Product
# Register your models here.
class CatAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Category,CatAdmin)

class ProdAdmin(admin.ModelAdmin):
    list_display = ['name','price','stock','available','created','updated']
    list_editable = ['price','stock','available']
    prepopulated_fields = {'slug':('name',)}
    list_per_page = 20

admin.site.register(Product,ProdAdmin)

