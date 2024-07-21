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
            name='Inventory',
            fields=[
                ('device_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('serial_number', models.CharField(max_length=255, unique=True)),
                ('location', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('discovered_device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scan.discovereddevice')),
            ],
        ),
    ]
