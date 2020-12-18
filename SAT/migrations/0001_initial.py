# Generated by Django 2.2.16 on 2020-12-18 23:13

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
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section', models.CharField(max_length=30)),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SAT.Test')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('questions_text', models.CharField(max_length=400)),
                ('passage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SAT.Passage')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SAT.Section')),
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
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(blank=True, default='', max_length=500)),
                ('choice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SAT.Choice')),
            ],
        ),
    ]
