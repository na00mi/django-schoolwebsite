# Generated by Django 2.2.16 on 2021-05-28 12:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0007_auto_20210528_2122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='subject',
            field=models.ForeignKey(default='0000', on_delete=django.db.models.deletion.CASCADE, to='schedule.Subject'),
        ),
    ]
