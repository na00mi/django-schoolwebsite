# Generated by Django 2.2.16 on 2021-05-28 12:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0008_auto_20210528_2124'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='subj_subname',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subname_assign', to='schedule.Subject'),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule.Subject'),
        ),
    ]