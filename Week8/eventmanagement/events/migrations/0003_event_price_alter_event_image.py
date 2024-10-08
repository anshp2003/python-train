# Generated by Django 5.1 on 2024-09-04 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_alter_event_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='events/'),
        ),
    ]
