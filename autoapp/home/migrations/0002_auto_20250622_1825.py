# Generated by Django 3.2 on 2025-06-22 18:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='riderequest',
            name='accepted_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='accepted_rides', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='riderequest',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
