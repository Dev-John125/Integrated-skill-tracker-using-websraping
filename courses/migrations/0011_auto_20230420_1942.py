# Generated by Django 3.2.17 on 2023-04-20 14:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0010_auto_20230419_0858'),
    ]

    operations = [
        migrations.CreateModel(
            name='CodingQuestion',
            fields=[
                ('question_no', models.AutoField(primary_key=True, serialize=False)),
                ('question_name', models.CharField(max_length=1000)),
                ('question_link', models.CharField(max_length=10000)),
                ('question_difficulty', models.CharField(choices=[('medium', 'Medium'), ('hard', 'Hard'), ('easy', 'Easy')], default='easy', max_length=10)),
                ('question_type', models.CharField(choices=[('linkedlist', 'Linkedlist'), ('binary search tree', 'Binary Search Tree'), ('backtracking', 'Backtracking'), ('stack & queue', 'Stack & Queue'), ('heap', 'Heap'), ('dynamic programming', 'Dynamic Programming'), ('searching & sorting', 'Searching & Sorting'), ('graph', 'Graph'), ('bit maniputation', 'Bit Maniputaion'), ('trie', 'Trie'), ('greedy', 'Greedy'), ('string', 'String'), ('binary tree', 'Binary Tree'), ('array', 'Array '), ('matrix', 'Matrix')], default='array', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='UserCodingQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_done', models.BooleanField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.codingquestion')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'question')},
            },
        ),
        migrations.DeleteModel(
            name='ContestQuestion',
        ),
    ]