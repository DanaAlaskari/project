# Generated by Django 3.1 on 2023-12-19 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reviews', '0009_auto_20231218_1800'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='email',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
