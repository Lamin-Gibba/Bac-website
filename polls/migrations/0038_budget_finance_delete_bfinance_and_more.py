# Generated by Django 5.0.4 on 2024-08-17 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0037_planing_and_dev_delete_plananddev'),
    ]

    operations = [
        migrations.CreateModel(
            name='Budget_finance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bg_image', models.ImageField(blank=True, null=True, upload_to='img/')),
                ('mandate_para', models.TextField(blank=True, null=True)),
                ('image_finas', models.ImageField(blank=True, null=True, upload_to='img/')),
                ('content_p1', models.TextField(blank=True, null=True)),
                ('content_p2', models.TextField(blank=True, null=True)),
                ('content_p3', models.TextField(blank=True, null=True)),
                ('content_p4', models.TextField(blank=True, null=True)),
                ('content_p5', models.TextField(blank=True, null=True)),
                ('content_p6', models.TextField(blank=True, null=True)),
                ('content_p7', models.TextField(blank=True, null=True)),
                ('content_p8', models.TextField(blank=True, null=True)),
                ('content_p9', models.TextField(blank=True, null=True)),
                ('content_p10', models.TextField(blank=True, null=True)),
                ('content_p11', models.TextField(blank=True, null=True)),
                ('content_p12', models.TextField(blank=True, null=True)),
                ('content_p13', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Bfinance',
        ),
        migrations.RenameField(
            model_name='planing_and_dev',
            old_name='image_chaim',
            new_name='image_plan',
        ),
        migrations.AlterField(
            model_name='councilmembers',
            name='Title_name_mason',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
