from django.db import models

# Create your models here.

class Agent(models.Model):
    agent_id = models.IntegerField(null=True)
    name = models.CharField(max_length=50, null=True)
    qa = models.FloatField(null=True)
    ce = models.FloatField(null=True)
    csat = models.FloatField(null=True)
    aht = models.DurationField(null=True)
    hc = models.FloatField(null=True)
    
    def __str__(self):
        return self.name