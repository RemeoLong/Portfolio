# Generated by Django 2.2.16 on 2020-12-17 23:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Explanation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('explain_text', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Passage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('passage_text', models.CharField(max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('questions_text', models.CharField(max_length=400)),
                ('passage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SAT.Passage')),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=200)),
                ('correct', models.CharField(choices=[('Correct', 'Correct'), ('Incorrect', 'Incorrect')], default='Incorrect', max_length=10)),
                ('answer', models.CharField(blank=True, default='', max_length=500)),
                ('explain', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='SAT.Explanation')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SAT.Question')),
            ],
        ),
    ]
