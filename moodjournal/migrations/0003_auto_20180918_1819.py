# Generated by Django 2.1 on 2018-09-19 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moodjournal', '0002_auto_20180916_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journalentry',
            name='mood_date',
            field=models.DateField(auto_now=True),
        ),
    ]
