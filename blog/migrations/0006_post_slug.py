# Generated by Django 4.2.3 on 2023-11-01 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_post_dislike_post_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default=2, max_length=300),
            preserve_default=False,
        ),
    ]
