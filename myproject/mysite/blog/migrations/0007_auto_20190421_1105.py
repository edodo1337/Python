# Generated by Django 2.1.7 on 2019-04-21 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20190421_1103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(upload_to='media/images/<function Article.generate_filename at 0x0355B468>'),
        ),
    ]
