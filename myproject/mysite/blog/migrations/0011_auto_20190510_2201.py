# Generated by Django 2.1.7 on 2019-05-10 19:01

import blog.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='content',
            new_name='body',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='object_id',
        ),
        migrations.AddField(
            model_name='comment',
            name='article',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='blog.Article'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='image',
            field=models.ImageField(default=1, upload_to=blog.models.generate_filename),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(blank=True, on_delete=models.SET('anonymous'), to=settings.AUTH_USER_MODEL),
        ),
    ]
