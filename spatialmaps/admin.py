# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Post, Category, Author, Tag, NewsletterUser

# Register your models here.
class PostAdmin(admin.ModelAdmin):
	exclude = ['posted']
	prepopulated_fields = {'slug' : ('title',)}

class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug' : ('title',)}

class TagAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug' : ('title',)}

class NewsletterAdmin(admin.ModelAdmin):
	list_display = ('email', 'date_added',)

admin.site.register(NewsletterUser, NewsletterAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Author)
