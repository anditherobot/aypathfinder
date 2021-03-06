# Generated by Django 3.1.4 on 2020-12-05 06:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ayregistration', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegistrationCheckList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration_completed', models.BooleanField(default=False, verbose_name='Registration/ Re-Enrollment form completed and signed')),
                ('health_completed', models.BooleanField(default=False, verbose_name='Health form completed and signed')),
                ('registration_fee', models.BooleanField(default=False, verbose_name='Registration/ Re-Enrollment fee')),
                ('registration_fee_amount', models.IntegerField(default=False, verbose_name='Registration Fee Amount')),
                ('prior_fees', models.BooleanField(default=False, verbose_name='Prior year unpaid club dues')),
                ('prior_fees_amount', models.IntegerField(default=False, verbose_name='Prior year Fee Amount')),
                ('atlantic_fees', models.BooleanField(default=False, verbose_name='Atlantic Union Camporee fee (with form)')),
                ('atlantic_fees_amount', models.IntegerField(default=False, verbose_name='Atlantic Union Camporee fee Amount')),
                ('bayda_fees', models.BooleanField(default=False, verbose_name='BAYDA Youth congress fee/deposit')),
                ('bayda_fees_amount', models.IntegerField(default=False, verbose_name='BAYDA Youth congress fee/deposit Amount')),
                ('other_fees', models.BooleanField(default=False, verbose_name='Other')),
                ('other_fees_amount', models.IntegerField(default=False, verbose_name='Other Amount')),
                ('class_assigned', models.CharField(blank=True, max_length=50, verbose_name='Assigned to class.')),
                ('unit_assigned', models.CharField(blank=True, max_length=50, verbose_name='Placed in unit.')),
                ('package_workbook', models.BooleanField(default=False, verbose_name='Class workbook (welcome letter, code of conduct, points policy, Uniform FAQ, current year program schedule)')),
                ('package_pathfindertshirt', models.BooleanField(default=False, verbose_name='Pathfinder t-shirt(to new Pathfinder only, if not given in prior year)')),
                ('package_sweatshirt', models.BooleanField(default=False, verbose_name='Pathfinder sweat shirt(to new Pathfinder only, if not given in prior year)')),
                ('package_adventurertshirt', models.BooleanField(default=False, verbose_name='Adventurer t-shirt (to new Pathfinder only, if not given in prior year)')),
                ('package_namebadge', models.CharField(blank=True, max_length=100, verbose_name='Name badge for')),
                ('date_updated', models.DateField(blank=True, null=True, verbose_name='Date Updated')),
                ('registrant', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='ayregistration.registrantinfo')),
            ],
        ),
    ]
