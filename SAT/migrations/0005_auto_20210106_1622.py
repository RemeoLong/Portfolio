# Generated by Django 2.2.16 on 2021-01-06 22:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SAT', '0004_answer_choice'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='answer',
            options={'ordering': ('User', 'answer')},
        ),
        migrations.RenameField(
            model_name='answer',
            old_name='UserID',
            new_name='User',
        ),
    ]
