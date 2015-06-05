from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader
from django.db.models import Count
from django.shortcuts import render_to_response
from django.template import RequestContext

# Create your views here.
from food.models import Vendors
from food.models import Events
from food.facebook_api import FacebookAPI

#Home View
def index(request):
	#update_foodtrucks(request)
	t = loader.get_template('vendors/home.html')
	c = Context({})
	return HttpResponse(t.render(c))
	
#Events View	
def get_events(request):
	events = Events.objects.all()
	context = {
		'events': events
	}
	return render_to_response(
    'vendors/events.html',
    context,
    context_instance = RequestContext(request),
	)

#List of event vendors	
def get_event_vendors(request, event_location):
	vendors = Vendors.objects.filter(location=event_location)
	return render_to_response(
    'vendors/event_vendors.html',
    {'vendors':vendors},
    context_instance = RequestContext(request),
	)	

#Vendor View
def get_vendor_name(request, vendor_id):
	count="0"
	foodtrucks = Vendors.objects.values('name'). \
		annotate(vendor_count=Count('name'))
	vendor = Vendors.objects.filter(id=vendor_id)
	v = vendor.values_list('name')[0][0]
	for e in foodtrucks:
		if  v == e['name']:
			count=e['vendor_count']
	return render_to_response(
    'vendors/vendor.html',
    {'vendor':vendor,'count':count},
    context_instance = RequestContext(request),
  )

#Vendors View  
def get_foodtrucks(request):
  foodtrucks = Vendors.objects.values('name'). \
    annotate(vendor_count=Count('name')). \
    order_by('-vendor_count')
  for e in foodtrucks:
	x = getid(e['name'])
	e['id']=x
	#print e
  #print foodtrucks
  context = {
    'foodtrucks': foodtrucks,
  }
  return render_to_response(
    'vendors/foodtruck.html',
    context,
    context_instance = RequestContext(request),
  )

def getid(name):
	vendors=Vendors.objects.all()
	for e in vendors:
		if e.name == name:
			#print e.id
			return e.id
  
def update_foodtrucks(request):
  fb = FacebookAPI()
  fb_json = fb.get_facebook_json()
  
  foodtrucks = Vendors.objects. \
    values_list('name'). \
    annotate(truck_count=Count('name')). \
    order_by('-truck_count')
  
  context = {
    'foodtrucks': foodtrucks,
  }
  return render_to_response(
    'vendors/foodtruck.html',
    context,
    context_instance = RequestContext(request),
  )