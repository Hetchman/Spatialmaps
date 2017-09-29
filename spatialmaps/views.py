# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse
from .models import Post, Category, NewsletterUser
from .forms import NewsletterUserSignUpForm

# Create your views here.
# def index(request):
# 	return HttpResponse(" Hello this is the test")

def home(request):
	form = NewsletterUserSignUpForm(request.POST or None)

	if form.is_valid():
		instance = form.save(commit=False)
		if NewsletterUser.objects.filter(email=instance.email).exists():
			print("Sorry this email already exists")
		else:
			instance.save()

	context = {
		'form' : form,
	}
	
	return render(request, 'spatialmaps/free.html', context)

def gis_services(request):
	return render(request, 'spatialmaps/gis_services.html')

def remote_sensing(request):
	return render(request, 'spatialmaps/remote_sensing.html')

def surveying_mapping(request):
	return render(request, 'spatialmaps/surveying_mapping.html')	

def technical_training(request):
	return render(request, 'spatialmaps/technical_training.html')

def industries(request):
	return render(request, 'spatialmaps/industries.html')

def agriculture_forestry(request):
	return render(request, 'spatialmaps/agriculture_forestry.html')

def land_admin_and_management(request):
	return render(request, 'spatialmaps/land_admin_and_management.html')

def marketing_and_advertisement(request):
	return render(request, 'spatialmaps/marketing_and_advertisement.html')

def national_regional_governance(request):
	return render(request, 'spatialmaps/national_regional_governance.html')

def natural_resources(request):
	return render(request, 'spatialmaps/natural_resources.html')	

def real_estate_property(request):
	return render(request, 'spatialmaps/real_estate_property.html')

def security_disaster_management(request):
	return render(request, 'spatialmaps/security_disaster_management.html')	

def urban_rural_development(request):
	return render(request, 'spatialmaps/urban_rural_development.html')

def water_resources(request):
	return render(request, 'spatialmaps/water_resources.html')

def news(request):
	return render(request, 'spatialmaps/news.html')

def blog(request):
	return render(request, 'spatialmaps/blog.html')

def events(request):
	return render_to_response('spatialmaps/events.html', {
		'categories' : Category.objects.all(),
		'posts' : Post.objects.all()[:5]
		})

def products(request):
	return render(request, 'spatialmaps/products.html')

def contact(request):
	return render(request, 'spatialmaps/contact.html')

def about_us(request):
	return render(request, 'spatialmaps/About_us.html')

def careers(request):
	return render(request, 'spatialmaps/careers.html')\

def partners(request):
	return render(request, 'spatialmaps/partners.html')										

def view_post(request, slug):
	return render_to_response('spatialmaps/view_post.html',
		{
		'post' : get_object_or_404(Post, slug=slug)
		})

def view_category(request, slug):
	category = get_object_or_404(Category, slug=slug)
	return render_to_response('spatialmaps/view_category.html', {
		'category' : category,
		'posts' : Post.objects.filter(category=category)[:5]
		})											
		
def newsletter_signup(request):
	form = NewsletterUserSignUpForm(request.POST or None)

	if form.is_valid():
		instance = form.save(commit=False)
		if NewsletterUser.objects.filter(email=instance.email).exists():
			print("Sorry this email already exists")
		else:
			instance.save()

	context = {
		'form' : form,
	}
	template = 'spatialmaps/sign_up.html'
	return render(request, template, context)

def newsletter_unsubscribe(request):
	form = NewsletterUserSignUpForm(request.POST or None)

	if form.is_valid():
		instance = form.save(commit=False)
		if NewsletterUser.objects.filter(email=instance.email).exists():
			NewsletterUser.objects.filter(email=instance.email).delete()
		else:
			print('Sorry but we did not find your email address')

	context = {
		"form" : form,
	}

	template = 'spatialmaps/unsubscribe.html'
	return render(request, template, context)									