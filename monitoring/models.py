from django.db import models
import uuid
from scan.models import DiscoveredDevice
# Create your models here.

class SnmpEnabledDevice(models.Model):
    snmp_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    device_id = models.ForeignKey(DiscoveredDevice, on_delete=models.CASCADE)
    ip_address = models.CharField(max_length=15)
    community_string = models.CharField(max_length=255)
    sys_name = models.CharField(max_length=255, blank=True, null=True)
    sys_desc = models.TextField(blank=True, null=True)
    sys_uptime = models.CharField(max_length=255, blank=True, null=True)
    last_checked = models.DateTimeField(auto_now_add=True)

class Monitoring(models.Model):
    monitor_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    device_id = models.ForeignKey(DiscoveredDevice, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    cpu_utilization = models.FloatField()
    memory_utilization = models.FloatField()
    traffic_in = models.FloatField()
    traffic_out = models.FloatField()
    status = models.CharField(max_length=50)
