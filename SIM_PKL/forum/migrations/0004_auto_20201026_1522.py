# Generated by Django 3.1.2 on 2020-10-26 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0003_auto_20201015_1153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='komen',
            name='komentar',
            field=models.CharField(max_length=100),
        ),
    ]
