# Generated by Django 3.1.7 on 2021-04-08 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parking', '0008_bookedplots_plot_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookedplots',
            name='is_exited',
            field=models.BooleanField(default=False),
        ),
    ]
