# Generated by Django 4.0.5 on 2022-07-11 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_auto_mascota'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auto',
            name='año',
            field=models.CharField(max_length=4),
        ),
    ]
