# Generated by Django 2.1.2 on 2018-11-16 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NextDoor', '0008_auto_20181116_1414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='date',
            field=models.CharField(max_length=100),
        ),
    ]
