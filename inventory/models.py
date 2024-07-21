from django.db import models
import uuid
from scan.models import DiscoveredDevice
# Create your models here.

class Inventory(models.Model):
    device_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    discovered_device = models.ForeignKey(DiscoveredDevice, on_delete=models.CASCADE)
    serial_number = models.CharField(max_length=255, unique=True)
    location = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
