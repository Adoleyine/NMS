from django.db import models
import uuid

# Create your models here.
class DiscoveredDevice(models.Model):
    device_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ip_address = models.CharField(max_length=15)
    mac_address = models.CharField(max_length=17)
    vendor = models.CharField(max_length=255, blank=True, null=True)
    last_discovered = models.DateTimeField(auto_now_add=True)
