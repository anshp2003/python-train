# Generated by Django 5.1 on 2024-08-21 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory1', '0003_tag_alter_item1_category_item5'),
    ]

    operations = [
        migrations.AddField(
            model_name='item5',
            name='quantity',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
