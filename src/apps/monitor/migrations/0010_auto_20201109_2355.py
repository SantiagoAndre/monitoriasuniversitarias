# Generated by Django 3.1.2 on 2020-11-10 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0009_monitor_informatic_tool'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monitor',
            name='informatic_tool',
            field=models.CharField(default=False, max_length=2, null=True),
        ),
    ]
