# Generated by Django 3.0.5 on 2020-08-21 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='name',
            field=models.CharField(default='Unknow', max_length=100),
        ),
    ]
