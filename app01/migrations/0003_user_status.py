# Generated by Django 2.2.3 on 2019-07-23 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_auto_20190721_1014'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='status',
            field=models.IntegerField(default=0, max_length=1),
        ),
    ]
