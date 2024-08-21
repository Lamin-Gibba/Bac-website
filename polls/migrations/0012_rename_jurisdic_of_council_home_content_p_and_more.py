# Generated by Django 5.0.4 on 2024-08-06 13:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0011_remove_home_aerial_space_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='home',
            old_name='Jurisdic_of_Council',
            new_name='content_p',
        ),
        migrations.RenameField(
            model_name='home',
            old_name='image_about_BAC',
            new_name='featured_image',
        ),
        migrations.RenameField(
            model_name='home',
            old_name='Descriptio_ceo',
            new_name='title_name',
        ),
        migrations.RemoveField(
            model_name='home',
            name='Description_busim',
        ),
        migrations.RemoveField(
            model_name='home',
            name='Description_chairm',
        ),
        migrations.RemoveField(
            model_name='home',
            name='Description_headqut',
        ),
        migrations.RemoveField(
            model_name='home',
            name='Description_nurs',
        ),
        migrations.RemoveField(
            model_name='home',
            name='Description_teacher',
        ),
        migrations.RemoveField(
            model_name='home',
            name='Description_vice',
        ),
        migrations.RemoveField(
            model_name='home',
            name='Natural_Resoures',
        ),
        migrations.RemoveField(
            model_name='home',
            name='Pop_density',
        ),
        migrations.RemoveField(
            model_name='home',
            name='Population',
        ),
        migrations.RemoveField(
            model_name='home',
            name='Public_and_Enviro_Health',
        ),
        migrations.RemoveField(
            model_name='home',
            name='Road_Ntw_Infras',
        ),
        migrations.RemoveField(
            model_name='home',
            name='Testim_busim',
        ),
        migrations.RemoveField(
            model_name='home',
            name='Testim_name_teacher',
        ),
        migrations.RemoveField(
            model_name='home',
            name='Testim_nurs',
        ),
        migrations.RemoveField(
            model_name='home',
            name='Title_name_ceo',
        ),
        migrations.RemoveField(
            model_name='home',
            name='Title_name_chairman',
        ),
        migrations.RemoveField(
            model_name='home',
            name='Title_name_vice',
        ),
        migrations.RemoveField(
            model_name='home',
            name='Yearly_Pop_shift',
        ),
        migrations.RemoveField(
            model_name='home',
            name='aerial_space',
        ),
        migrations.RemoveField(
            model_name='home',
            name='content_BAC',
        ),
        migrations.RemoveField(
            model_name='home',
            name='content_Local_Tailored',
        ),
        migrations.RemoveField(
            model_name='home',
            name='content_about_BAC',
        ),
        migrations.RemoveField(
            model_name='home',
            name='description_bAC',
        ),
        migrations.RemoveField(
            model_name='home',
            name='image_basseAC',
        ),
        migrations.RemoveField(
            model_name='home',
            name='telephone_CallUs',
        ),
        migrations.RemoveField(
            model_name='home',
            name='telephone_reach_out',
        ),
        migrations.RemoveField(
            model_name='home',
            name='testim_image_busim',
        ),
        migrations.RemoveField(
            model_name='home',
            name='testim_image_nurs',
        ),
        migrations.RemoveField(
            model_name='home',
            name='testim_image_teacher',
        ),
        migrations.RemoveField(
            model_name='home',
            name='title_image_ceo',
        ),
        migrations.RemoveField(
            model_name='home',
            name='title_image_chairm',
        ),
        migrations.RemoveField(
            model_name='home',
            name='title_image_vice',
        ),
        migrations.RemoveField(
            model_name='home',
            name='words_busim',
        ),
        migrations.RemoveField(
            model_name='home',
            name='words_nurs',
        ),
        migrations.RemoveField(
            model_name='home',
            name='words_teach',
        ),
    ]
