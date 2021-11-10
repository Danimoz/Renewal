# Generated by Django 3.2.8 on 2021-11-01 11:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Trademark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trademarkName', models.CharField(max_length=100)),
                ('trademarkClass', models.CharField(max_length=100)),
                ('datePosted', models.DateTimeField(default=django.utils.timezone.now)),
                ('acknowledgeDoc', models.FileField(upload_to='')),
                ('acceptanceDoc', models.FileField(upload_to='')),
                ('cert', models.FileField(upload_to='')),
                ('renewalDoc', models.FileField(upload_to='')),
                ('shelfLife', models.DateTimeField()),
                ('uploadedBy', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Container',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productName', models.CharField(max_length=100)),
                ('containerNo', models.CharField(max_length=100)),
                ('agentName', models.CharField(max_length=100)),
                ('receiptDoc', models.FileField(upload_to='')),
                ('endorsementDoc', models.FileField(upload_to='')),
                ('uploadBy', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
