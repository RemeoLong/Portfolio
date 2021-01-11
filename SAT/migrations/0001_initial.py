# Generated by Django 2.2.16 on 2021-01-11 21:51

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
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='TotalScore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(default=0)),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('section', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='SAT.Section')),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SAT.Test')),
            ],
            options={
                'ordering': ('User', 'test', 'section', 'score'),
            },
        ),
        migrations.AddField(
            model_name='section',
            name='test',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='SAT.Test'),
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('questions_text', models.CharField(max_length=400)),
                ('passage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SAT.Passage')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SAT.Section')),
                ('test', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='SAT.Test')),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=200)),
                ('correct', models.CharField(choices=[('Correct', 'Correct'), ('Incorrect', 'Incorrect')], default='Incorrect', max_length=10)),
                ('explain', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='SAT.Explanation')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SAT.Question')),
            ],
            options={
                'ordering': ('question', 'choice_text', 'correct'),
            },
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(blank=True, default='', max_length=500)),
                ('User', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('question', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='SAT.Question')),
            ],
            options={
                'ordering': ('User', 'answer'),
            },
        ),
    ]
