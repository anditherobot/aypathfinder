# Generated by Django 3.1.4 on 2020-12-09 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ayregistration', '0002_registrationchecklist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registrantinfo',
            name='apt_number',
        ),
        migrations.AlterField(
            model_name='registrantinfo',
            name='ifyespathfinder',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='at'),
        ),
        migrations.AlterField(
            model_name='registrantinfo',
            name='phone_number',
            field=models.CharField(max_length=50, verbose_name='Phone #'),
        ),
    ]
