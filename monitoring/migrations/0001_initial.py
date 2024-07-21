# Generated by Django 5.0.7 on 2024-07-21 17:37

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('scan', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Monitoring',
            fields=[
                ('monitor_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('cpu_utilization', models.FloatField()),
                ('memory_utilization', models.FloatField()),
                ('traffic_in', models.FloatField()),
                ('traffic_out', models.FloatField()),
                ('status', models.CharField(max_length=50)),
                ('device_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scan.discovereddevice')),
            ],
        ),
        migrations.CreateModel(
            name='SnmpEnabledDevice',
            fields=[
                ('snmp_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('ip_address', models.CharField(max_length=15)),
                ('community_string', models.CharField(max_length=255)),
                ('sys_name', models.CharField(blank=True, max_length=255, null=True)),
                ('sys_desc', models.TextField(blank=True, null=True)),
                ('sys_uptime', models.CharField(blank=True, max_length=255, null=True)),
                ('last_checked', models.DateTimeField(auto_now_add=True)),
                ('device_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scan.discovereddevice')),
            ],
        ),
    ]
