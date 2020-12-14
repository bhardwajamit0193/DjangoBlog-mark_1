from django.contrib import admin
from .models import Post, Categorie, Author, Subscribe, Contact

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=('title','slug','author','publish','status',)
    list_filter=('status','created','publish','author')
    search_fields=('title','body')
    prepopulated_fields={'slug':('title',)}
    raw_id_fields=('author',)
    date_hierarchy='publish'
    ordering=('-status','-publish')

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display=('fname','lname','email','time')
    ordering=('-time',)
    list_filter=('fname','lname','email','time')



   


admin.site.register(Categorie)
admin.site.register(Author)
admin.site.register(Subscribe)

