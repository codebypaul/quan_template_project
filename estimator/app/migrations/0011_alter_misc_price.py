# Generated by Django 5.0.3 on 2024-05-23 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_alter_chinaparts_collection'),
    ]

    operations = [
        migrations.AlterField(
            model_name='misc',
            name='price',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
