# Generated by Django 2.0.8 on 2020-04-14 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20200306_0220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='occupation',
            field=models.CharField(default='', max_length=100),
        ),
    ]
