# Generated by Django 5.1 on 2024-08-11 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mobile',
            name='status',
            field=models.CharField(choices=[('+', '+'), ('-', '-')], max_length=10),
        ),
    ]
