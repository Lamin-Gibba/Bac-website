# Generated by Django 5.0.4 on 2024-08-06 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0016_home_quote_nat_resourse_home_quote_enviro_health'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='telephone_CallUs',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='home',
            name='telephone_reach_out',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
