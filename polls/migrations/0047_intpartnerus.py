# Generated by Django 5.0.4 on 2024-08-27 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0046_partnerus'),
    ]

    operations = [
        migrations.CreateModel(
            name='IntpartnerUS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
                ('organization', models.CharField(blank=True, max_length=100, null=True)),
                ('select', models.SlugField(blank=True, null=True)),
                ('message', models.TextField()),
            ],
        ),
    ]
