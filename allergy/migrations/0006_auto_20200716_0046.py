# Generated by Django 3.0.4 on 2020-07-15 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allergy', '0005_auto_20200716_0034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allergy',
            name='New_Allergy',
            field=models.CharField(max_length=70),
        ),
    ]
