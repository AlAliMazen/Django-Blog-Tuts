from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Comment


# creating the summernote
@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'status','created_on')
    search_fields = ['title','content']
    list_filter = ('status','created_on',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)

# Register your models here.
#admin.site.register(Post)
@admin.register(Comment)
class CommentAdmin(SummernoteModelAdmin):
    list_display = ('author', 'approved', 'content')
