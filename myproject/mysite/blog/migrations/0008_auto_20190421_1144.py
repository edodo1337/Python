# Generated by Django 2.1.7 on 2019-04-21 08:44

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20190421_1105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(upload_to=blog.models.generate_filename),
        ),
    ]
