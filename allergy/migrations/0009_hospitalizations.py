# Generated by Django 3.0.4 on 2020-07-17 15:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('allergy', '0008_delete_hospitalizations'),
    ]

    operations = [
        migrations.CreateModel(
            name='hospitalizations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateCreated', models.DateField(auto_now_add=True)),
                ('dateCompleted', models.DateField(blank=True, null=True)),
                ('Name_of_hospital', models.CharField(max_length=100)),
                ('photo', models.ImageField(upload_to='hospitalizations')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
