# Generated by Django 5.1 on 2024-11-12 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serveradmin', '0005_history'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='file_path',
            field=models.FileField(default=0, upload_to='uploads/'),
            preserve_default=False,
        ),
    ]
