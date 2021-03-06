# Generated by Django 3.0.5 on 2020-08-20 13:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.CharField(max_length=36, primary_key=True, serialize=False)),
                ('idEmployee', models.CharField(blank=True, max_length=36)),
                ('idVisitor', models.CharField(max_length=36)),
                ('typeVisit', models.IntegerField(choices=[(1, 'Meeting'), (2, 'Package'), (3, 'General')], default=1)),
                ('dateVisit', models.DateField(default=datetime.date(2020, 8, 20))),
                ('hourVisit', models.TimeField(default=datetime.time(12, 0))),
                ('status', models.IntegerField(choices=[(1, 'Scheduled'), (2, 'Started'), (3, 'Finished'), (4, 'Cancelled')], default=1)),
            ],
        ),
    ]
