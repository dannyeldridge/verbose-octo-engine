# Generated by Django 2.1 on 2018-09-16 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moodjournal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journalentry',
            name='mood_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]