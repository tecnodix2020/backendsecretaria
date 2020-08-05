# Generated by Django 3.0.5 on 2020-08-05 18:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='visits',
            name='hourVisit',
            field=models.TimeField(default=datetime.time(12, 0)),
        ),
        migrations.AlterField(
            model_name='visits',
            name='dateVisit',
            field=models.DateField(),
        ),
    ]
