# Generated by Django 3.1.5 on 2021-09-29 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20210915_1813'),
    ]

    operations = [
        migrations.CreateModel(
            name='PendingAppointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_name', models.CharField(max_length=30)),
                ('e_name', models.CharField(max_length=30)),
                ('service', models.CharField(max_length=30)),
                ('problem', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=30)),
                ('time', models.CharField(max_length=30)),
            ],
        ),
    ]