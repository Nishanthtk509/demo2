# Generated by Django 3.2 on 2021-04-21 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapps', '0002_auto_20210420_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_login',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='tbl_registrations',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
