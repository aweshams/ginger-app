from django.db import models
from datetime import datetime, timedelta

# Create your models here.
class Vendors(models.Model):
  name = models.CharField(max_length=30)
  location = models.CharField(max_length=300, null=True, blank=True)
  start_date = models.DateField(null=True, blank=True)
  #start_time = models.TimeField(null=True, blank=True)

  def __unicode__(self):
    return self.name 

  def save(self, **kwargs):
    ft = Vendors.objects.filter(name = self.name, 
                                  location = self.location)
    if not ft:
      super(Vendors, self).save(**kwargs)

  def last_month():
    now = datetime.now()
    start = datetime.min.replace(year=now.year, month=now.month,
                                 day=now.day)
    end = (start + timedelta(days=30)) - timedelta.resolution
    return (start, end)
	
class Events(models.Model):
  name = models.CharField(max_length=30)
  location = models.CharField(max_length=300, null=True, blank=True)
  def __unicode__(self):
    return self.name 

  def save(self, **kwargs):
    ft = Events.objects.filter(name = self.name, 
                                  location = self.location)
    if not ft:
      super(Events, self).save(**kwargs)