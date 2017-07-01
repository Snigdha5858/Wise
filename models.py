from django.db import models

class Profile(models.Model):
      Userid = models.IntegerField()
      City_State_areaid = models.Integerfield()
      PhoneNumber = models.IntegerField()
class Feedback(models.Model):
      Userid = models.IntegerField()
      feedback = models.CharField(max_length = 30)
      created_date = models.DateTimeField(default= timezone.now)
class Locations(models.Model):
      Name = models.CharField(max_length = 40)
      Address = models.CharField(max_length = 40)
      Landmark = models.CharField(max_length = 30)
      City_State_areaid = models.IntegerField()
      Rating = models.IntegerField()
      Location_typeid = models.IntegerField()
class LocationTypes(models.Model):
      Location_id = models.IntegerField()
      Location_type = models.CharField(max_length = 30)
class State(models.Model):
      State_id = models.IntegerField()
      State_name = models.CharField(max_length= 30)
class City(models.Model):
      City_id = models.IntegerField()
      City_Name = models.CharField(max_length = 30)
class Area(models.Model):
      Area_id = models.IntegerField()
      Area_name = models.CharField(max_length = 30)
class State_City_Area(models.Model)
      City_State_areaid = models.IntegerField()
      City_id = models.IntegerField()
      Area_id = models.IntegerField()
class Notifications(models.Model)
      City_State_areaid = models.IntegerField()
      Event_name = models.CharField(max_length = 30)
      Date_Time = models.DateTimeField(default = timezone.now)
      
