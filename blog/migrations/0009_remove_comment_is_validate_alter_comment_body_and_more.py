# Generated by Django 4.2.3 on 2023-11-09 17:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_post_dislike_alter_post_like'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='is_validate',
        ),
        migrations.AlterField(
            model_name='comment',
            name='body',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.post'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='update_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
