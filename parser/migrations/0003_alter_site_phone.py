# Generated by Django 4.0.5 on 2022-06-15 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parser', '0002_rename_name_contact_person_site_thematic_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site',
            name='phone',
            field=models.TextField(blank=True, null=True, unique=True),
        ),
    ]
