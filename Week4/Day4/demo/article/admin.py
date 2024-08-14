from django.contrib import admin
from article.models import Article2  # Ensure this import is correct

class ArticleAdmin(admin.ModelAdmin):  # Class name should start with a capital letter
    search_fields = ['title']  # Ensure 'name' is a field in your model
    
admin.site.register(Article2, ArticleAdmin)
