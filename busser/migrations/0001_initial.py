# Generated by Django 3.1 on 2020-11-01 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Busser_Supplies_Requests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spray_bottle', models.BooleanField(default=False)),
                ('sanitizing_cloth', models.BooleanField(default=False)),
                ('carrying_tray', models.BooleanField(default=False)),
                ('request_complete', models.BooleanField(default=False)),
            ],
        ),
    ]
