# Generated by Django 4.1.3 on 2024-09-18 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('admin', 'Admin'), ('user', 'User')], default='user', max_length=5),
        ),
        migrations.AddField(
            model_name='user',
            name='unique_id',
            field=models.CharField(blank=True, max_length=8, unique=True),
        ),
    ]
