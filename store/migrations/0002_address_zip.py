# Generated by Django 4.1.7 on 2023-03-14 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='zip',
            field=models.CharField(default='10002', max_length=255),
        ),
    ]