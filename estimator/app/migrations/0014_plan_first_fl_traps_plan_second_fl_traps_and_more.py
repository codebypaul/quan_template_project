# Generated by Django 5.0.3 on 2024-07-08 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_plan'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='first_fl_traps',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='plan',
            name='second_fl_traps',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='plan',
            name='third_fl_traps',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
