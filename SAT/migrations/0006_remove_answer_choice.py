# Generated by Django 2.2.16 on 2021-01-07 19:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SAT', '0005_auto_20210106_1622'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='choice',
        ),
    ]
