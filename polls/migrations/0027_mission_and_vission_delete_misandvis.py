# Generated by Django 5.0.4 on 2024-08-08 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0026_aboutus_councillors_aboutus_constituencies_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='mission_and_vission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vission', models.TextField(blank=True, null=True)),
                ('mission', models.TextField(blank=True, null=True)),
                ('legal_mandate', models.TextField(blank=True, null=True)),
                ('image_mis_vis', models.ImageField(blank=True, null=True, upload_to='img/')),
            ],
        ),
        migrations.DeleteModel(
            name='MisandVis',
        ),
    ]
