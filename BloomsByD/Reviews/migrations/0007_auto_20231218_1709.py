# Generated by Django 3.1 on 2023-12-18 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reviews', '0006_review_flower'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='flower',
            field=models.TextField(default=''),
        ),
    ]