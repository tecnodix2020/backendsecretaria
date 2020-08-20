# Generated by Django 3.0.5 on 2020-08-20 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.CharField(max_length=36, primary_key=True, serialize=False)),
                ('companyName', models.CharField(max_length=100)),
                ('observation', models.CharField(blank=True, max_length=200)),
                ('availability', models.CharField(choices=[('1', 'Available'), ('0', 'Unavailable')], default='1', max_length=1)),
            ],
        ),
    ]
