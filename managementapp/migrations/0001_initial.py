# Generated by Django 4.2.5 on 2023-09-10 03:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='projectlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projects', models.CharField(max_length=500)),
                ('clients', models.CharField(max_length=500)),
                ('Duedate', models.DateField(blank=True, editable=False, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='manage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=120)),
                ('priority', models.IntegerField(choices=[(1, 'Normal'), (2, 'Urgent')])),
                ('projects', models.CharField(max_length=500)),
                ('Assigneto', models.CharField(max_length=200)),
                ('status', models.BooleanField(default=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
