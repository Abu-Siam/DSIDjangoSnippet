# Generated by Django 4.1.1 on 2022-09-28 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fileUploadDownload', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filedetailsmodel',
            name='owner',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
