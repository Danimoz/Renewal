# Generated by Django 3.2.8 on 2021-11-09 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20211107_2119'),
    ]

    operations = [
        migrations.AddField(
            model_name='container',
            name='expiryDate',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
