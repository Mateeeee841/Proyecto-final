# Generated by Django 4.0.5 on 2022-07-10 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='objetos',
            name='numero',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]