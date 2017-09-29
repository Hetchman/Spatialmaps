# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db.models import permalink

# Create your models here.
class Author(models.Model):
	'''
	1. Author name
	2. Author email (not mandatory)
	'''
	name = models.CharField(max_length=50)
	email = models.EmailField(unique=True)
	bio = models.TextField()

	def __unicode__(self):
		return self.name

class Post(models.Model):
	title = models.CharField(max_length=100, unique=True)
	slug = models.SlugField(max_length=100, unique=True)
	body = models.TextField()
	# posted = models.DateField(db_index=True, auto_now_add=True)
	category = models.ManyToManyField('spatialmaps.Category')
	created_date = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated_date = models.DateTimeField(auto_now_add=True, auto_now=False)
	author = models.ForeignKey('spatialmaps.Author')
	tags = models.ManyToManyField('spatialmaps.Tag')

	def __unicode__(self):
		return '%s' % self.title

	@permalink
	def get_absolute_url(self):
		return('view_post', None, {'slug' : self.slug})		

class Category(models.Model):
	title = models.CharField('category name', max_length=100, db_index=True)
	cat_description = models.CharField('category description', max_length=255)
	slug = models.SlugField(max_length=100, db_index=True)

	class Meta:
		verbose_name_plural = 'Categories'

	def __unicode__(self):
		return '%s' % self.title

	@permalink
	def get_absolute_url(self):
		return('view_category', None, {'slug' : self.slug})

class Tag(models.Model):
	title = models.CharField(max_length=50)
	tag_description = models.CharField(max_length=255)
	slug = models.SlugField(max_length=100, db_index=True)

	def __unicode__(self):
		return '%s' % self.title

	@permalink
	def get_absolute_url(self):
		return('view_tags', None, {'slug' : self.slug})

class NewsletterUser(models.Model):
	email = models.EmailField()
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.email