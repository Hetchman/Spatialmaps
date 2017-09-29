from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns = [
	# url(r'^$', views.index, name='index'),
	url(r'^home/$', views.home, name='home'),
	url(r'^news/$', views.news, name='news'),
	url(r'^blog/$', views.blog, name='blog'),
	url(r'^events/$', views.events, name='events'),
	url(r'^products/$', views.products, name='products'),
	url(r'^contact/$', views.contact, name='contact'),
	url(r'^gis_services/$', views.gis_services, name='gis_services'),
	url(r'^remote_sensing$', views.remote_sensing, name='remote_sensing'),
	url(r'^surveying_mapping/$', views.surveying_mapping, name='surveying_mapping'),
	url(r'^technical_training/$', views.technical_training, name='technical_training'),
	url(r'^industries/$', views.industries, name='industries'),
	url(r'^agriculture_forestry/$', views.agriculture_forestry, name='agriculture_forestry'),
	url(r'^land_admin_and_management/$', views.land_admin_and_management, name='land_admin_and_management'),
	url(r'^marketing_and_advertisement/$', views.marketing_and_advertisement, name='marketing_and_advertisement'),
	url(r'^national_regional_governance/$', views.national_regional_governance, name='national_regional_governance'),
	url(r'^natural_resources/$', views.natural_resources, name='natural_resources'),
	url(r'^water_resources/$', views.water_resources, name='water_resources'),
	url(r'^real_estate_propert/$', views.real_estate_property, name='real_estate_property'),
	url(r'^security_disaster_management/$', views.security_disaster_management, name='security_disaster_management'),
	url(r'^urban_rural_development/$', views.urban_rural_development, name='urban_rural_development'),
	url(r'^about_us/$', views.about_us, name='about_us'),
	url(r'^careers/$', views.careers, name='careers'),
	url(r'^partners/$', views.partners, name='partners'),
	url(r'^(?P<slug>[^\.]+)/view_post/$', views.view_post, name='view_post'),
	url(r'^(?P<slug>[^\.]+)/view_category/$', views.view_category, name='view_category'),
	url(r'^newsletter_signup/$', views.newsletter_signup, name='newsletter_signup'),
	url(r'^newsletter_unsubscribe/$', views.newsletter_unsubscribe, name='newsletter_unsubscribe'),


]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)