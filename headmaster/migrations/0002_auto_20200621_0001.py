# Generated by Django 2.2.6 on 2020-06-20 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('headmaster', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='headmaster_account',
            name='h_phone',
            field=models.CharField(max_length=11),
        ),
        migrations.AlterField(
            model_name='headmaster_verify',
            name='h_phone',
            field=models.CharField(max_length=11),
        ),
    ]
