# Generated by Django 2.1.3 on 2019-03-22 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0015_auto_20190321_2344'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='hab',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='edu',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='exp',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
    ]