from django.db import models

# Create your models here.
class Platform(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=200)
  
  def __str__(self):
    return self.name

class Status(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=200)

  def __str__(self):
    return self.name



class Edict(models.Model):
  id = models.AutoField(primary_key=True)
  proclamation = models.CharField(max_length=200)
  uasg = models.CharField(max_length=200)
  contractor = models.CharField(max_length=200)
  object = models.CharField(max_length=2000,blank=True, null=True)
  platform = models.ForeignKey(Platform, on_delete=models.PROTECT, related_name='edict_platform')
  start_date = models.DateField(blank=True, null=True)
  start_time = models.TimeField(blank=True, null=True)
  dispute_model = models.CharField(max_length=200)
  status = models.ForeignKey(Status, on_delete=models.PROTECT, related_name='edict_status')
  detail = models.TextField(blank=True, null=True)
  


class Archive(models.Model):
  id = models.AutoField(primary_key=True)
  edict = models.ForeignKey(Edict, on_delete=models.PROTECT, related_name='Archive_edict')
  archive = models.FileField(upload_to='edict/',blank=True, null=True)
  
  def __str__(self):
    return self.edict
