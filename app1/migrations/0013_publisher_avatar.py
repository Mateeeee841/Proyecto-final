# Generated by Django 4.0.5 on 2022-07-25 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0012_remove_publisher_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='publisher',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatars'),
        ),
    ]