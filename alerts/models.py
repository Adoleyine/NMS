from django.db import models
import uuid
from scan.models import DiscoveredDevice
# Create your models here.

class Alerts(models.Model):
    alert_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    device_id = models.ForeignKey(DiscoveredDevice, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    severity = models.CharField(max_length=50)
    message = models.TextField()
