# Generated by Django 4.2.6 on 2023-10-20 12:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_education_experience'),
        ('blog', '0003_alter_comment_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.userprofile'),
        ),
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.userprofile'),
        ),
    ]
