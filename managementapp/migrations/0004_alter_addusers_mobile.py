# Generated by Django 4.2.5 on 2023-09-10 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('managementapp', '0003_remove_addusers_user_addusers_designation_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addusers',
            name='mobile',
            field=models.CharField(max_length=200),
        ),
    ]
