# Generated by Django 2.2 on 2020-11-04 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0005_posting_upload_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posting',
            name='desc',
            field=models.TextField(max_length=2000),
        ),
    ]