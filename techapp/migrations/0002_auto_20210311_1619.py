# Generated by Django 3.1.2 on 2021-03-11 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('techapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='name',
            field=models.JSONField(),
        ),
    ]