# Generated by Django 5.1 on 2024-09-04 11:09

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_ticket'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], default='Pending', max_length=10),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='ticket_quantity',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
