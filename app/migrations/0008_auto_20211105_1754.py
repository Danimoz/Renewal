# Generated by Django 3.2.8 on 2021-11-05 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20211105_1747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='container',
            name='dateRenewed',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='trademark',
            name='dateRenewed',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
