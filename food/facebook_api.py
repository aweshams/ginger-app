import re, requests
from itertools import ifilter
from food.models import Vendors
from food.models import Events
from ginger_app import settings

class FacebookAPI():

  def __init__(self):
    # make these configurable variables
    self.base_fb_url = "https://graph.facebook.com/"
    self.access_token = settings.FACEBOOK_ACCESS_TOKEN

	
  def get_facebook_json(self, id = None):
    if not id:
		id = "OffTheGridSF/events?access_token="
		url = self.base_fb_url + id + self.access_token 
		#print url
		result = requests.get(url)
		if result.status_code == 200:
			data = result.json().get('data', [])
			if data:
				for names in data:
					event_names = names.get('name')
					location = names.get('id')
					#for event_name in event_names:
					if event_names:
						event = Events(name = event_names,
										location = location)
						event.save()
    else:
	  id = id+"?access_token="
    url = self.base_fb_url + id + self.access_token 
    #print url
    result = requests.get(url)
    if result.status_code == 200:
      results = result.json().get('data', [])
      if results:
        for ids in results:
          self.get_facebook_json(ids['id'])
      else:
        vendors = _parse_description_string(
                        result.json(). \
                        get('description', []))
        location = result.json().get('id')
        temp= result.json().get('start_time').split("T")
        start_date = temp[0]
        if vendors:
            for ven in vendors:
                if ven.strip() != '':
                    foodtruck = Vendors(name = ven.strip(),
                                          location = location, 
                                          start_date = start_date)
                    foodtruck.save()

	

def _parse_description_string(desc = None):
  if desc:
    desc_match1 = re.search(r'''(?sx)
         Vendors:(?P<vendors>.+?)(?:\n\r?){2}''', desc)
    desc_match2 = re.search(r'''(?sx)
         Food Truck Lineup (Subject to Change, Alternates every other week):(?P<vendors>.+?)(?:\,\r?){2}''', desc)
    desc_match3 = re.search(r'''(?sx)
         food trucks, including (?P<vendors>.+?)(?:\n\r?){2}''', desc)
    #print desc_match2
    if desc_match1:
        temp = desc_match1.group('vendors')
        #print temp
        return list(ifilter(None, 
                            re.split(r'(\s*\n|\r)+', 
                                     temp.strip())))
    elif desc_match2:
        temp = desc_match2.group('vendors')
        #print temp
        return list(ifilter(None, 
                            re.split(r'(\s*\n|\r)+', 
                                     temp.strip())))
    elif desc_match3:
        temp = desc_match3.group('vendors')
        return list(ifilter(None, 
                            re.split(r'(\s*\n|\r)+', 
                                     temp.strip())))
	

