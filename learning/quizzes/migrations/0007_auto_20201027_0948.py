# Generated by Django 3.1.2 on 2020-10-27 04:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_auto_20201019_1257'),
        ('quizzes', '0006_auto_20201025_2107'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='submitassignment',
            options={'verbose_name_plural': 'Submit Assignment'},
        ),
        migrations.AlterField(
            model_name='createquiz_2',
            name='data',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='quizzes.createquiz_1'),
        ),
        migrations.CreateModel(
            name='SubmitQuiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=20, null=True)),
                ('subject', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.course')),
                ('title', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='quizzes.createquiz_1')),
            ],
        ),
    ]
