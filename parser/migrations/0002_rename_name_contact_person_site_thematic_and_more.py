# Generated by Django 4.0.5 on 2022-06-15 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parser', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='site',
            old_name='name_contact_person',
            new_name='thematic',
        ),
        migrations.RenameField(
            model_name='site',
            old_name='url',
            new_name='website',
        ),
        migrations.RemoveField(
            model_name='site',
            name='themes',
        ),
        migrations.AddField(
            model_name='site',
            name='address',
            field=models.TextField(blank=True, max_length=70, null=True),
        ),
        migrations.AlterField(
            model_name='site',
            name='organisation',
            field=models.TextField(default='none', max_length=250),
            preserve_default=False,
        ),
    ]
