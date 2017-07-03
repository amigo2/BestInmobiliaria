from django.conf.urls import url
from . import views

app_name = 'listing'

urlpatterns = [
	
	#/listing
	url(r'^$', views.index, name='index'),



	#/listing/detail/215
	url(r'^(?P<property_id>[0-9]+)/$', views.details, name = 'details'),	

	#/listing/add
	url(r'create_property/$', views.PropertyCreate.as_view(),name='create_property'),


	#/listing/update
	url(r'^(?P<pk>[0-9]+)/update_property/$', views.PropertyUpdate.as_view(),name='update_property'),

	#/listing/delete
	#url(r'listing/(?P<property_id>[0-9]+)/delete/$', views.PropertyDelete.as_view(),name='delete_property'),
	url(r'^(?P<property_id>[0-9]+)/delete_property/$', views.delete_property, name='delete_property'),

	# register User not using the ^ ?
	url(r'register/$', views.UserFormView.as_view(),name='register'),
	


	]
	