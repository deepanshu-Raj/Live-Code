# Generated by Django 3.1.2 on 2020-10-29 19:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0009_merge_20201028_0057'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ques', models.CharField(max_length=100)),
                ('o1', models.CharField(max_length=100)),
                ('o2', models.CharField(max_length=100)),
                ('o3', models.CharField(max_length=100)),
                ('o4', models.CharField(max_length=100)),
                ('cans', models.CharField(max_length=100)),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizzes.createquiz_1')),
            ],
        ),
    ]