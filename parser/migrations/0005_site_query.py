# Generated by Django 4.0.5 on 2022-06-16 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parser', '0004_alter_site_address_alter_site_city_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='query',
            field=models.CharField(blank=True, max_length=70, null=True),
        ),
    ]
