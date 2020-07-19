# Generated by Django 3.0.4 on 2020-07-19 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allergy', '0011_hospitalization'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hospitalization',
            name='photo',
        ),
        migrations.AddField(
            model_name='hospitalization',
            name='description',
            field=models.TextField(default=False),
        ),
    ]