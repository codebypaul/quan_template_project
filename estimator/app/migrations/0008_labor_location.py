# Generated by Django 5.0.3 on 2024-05-20 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_labor_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='labor',
            name='location',
            field=models.CharField(blank=True, null=True),
        ),
    ]
