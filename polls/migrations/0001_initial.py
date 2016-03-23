# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-23 08:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import polls.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dialect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('name_in_language', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exercise_name', models.CharField(max_length=200, null=True)),
                ('instructions', models.CharField(max_length=500, null=True)),
                ('instructions_in_language', models.CharField(max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ExerciseQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_type', models.CharField(choices=[('ty', 'Typing'), ('tf', 'True or False'), ('dd', 'Drag and Drop'), ('mc', 'Multiple Choice')], default=('ty', 'Typing'), max_length=200)),
                ('question_text', models.CharField(max_length=200)),
                ('choice_1', models.CharField(blank=True, max_length=200)),
                ('choice_2', models.CharField(blank=True, max_length=200)),
                ('choice_3', models.CharField(blank=True, max_length=200)),
                ('choice_4', models.CharField(blank=True, max_length=200)),
                ('choice_5', models.CharField(blank=True, max_length=200)),
                ('choice_6', models.CharField(blank=True, max_length=200)),
                ('correct_answer', models.CharField(max_length=200)),
                ('exercise', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.Exercise')),
            ],
        ),
        migrations.CreateModel(
            name='ExerciseVocabularyQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=200)),
                ('choice_1', models.FileField(blank=True, default='', null=True, upload_to='', validators=[polls.models.validate_picture_extension])),
                ('choice_2', models.FileField(blank=True, default='', null=True, upload_to='', validators=[polls.models.validate_picture_extension])),
                ('choice_3', models.FileField(blank=True, default='', null=True, upload_to='', validators=[polls.models.validate_picture_extension])),
                ('choice_4', models.FileField(blank=True, default='', null=True, upload_to='', validators=[polls.models.validate_picture_extension])),
                ('choice_5', models.FileField(blank=True, default='', null=True, upload_to='', validators=[polls.models.validate_picture_extension])),
                ('choice_6', models.FileField(blank=True, default='', null=True, upload_to='', validators=[polls.models.validate_picture_extension])),
                ('correct_answer', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')], default=('1', '1'), max_length=1)),
                ('exercise', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.Exercise')),
            ],
        ),
        migrations.CreateModel(
            name='Glossary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(blank=True, max_length=50, null=True)),
                ('word_in_lang', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('name_in_language', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='LanguageSubtopic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subtopic_name', models.CharField(max_length=200, null=True)),
                ('subtopic_name_in_language', models.CharField(max_length=200, null=True)),
                ('grammar_video_file', models.FileField(blank=True, null=True, upload_to='', validators=[polls.models.validate_movie_extension])),
            ],
        ),
        migrations.CreateModel(
            name='LanguageTopic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic_name_in_language', models.CharField(blank=True, max_length=200)),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Language')),
            ],
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='LevelLanguage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Language')),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Level')),
            ],
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Alphabet', 'Alphabet'), ('Numbers', 'Numbers'), ('Days', 'Days of the Week'), ('Holidays', 'Holidays'), ('Months', 'Seasons and Months'), ('Time', 'Time')], default=0, max_length=200)),
                ('name_in_language', models.CharField(max_length=200)),
                ('instructions', models.CharField(max_length=200)),
                ('instructions_in_language', models.CharField(max_length=200)),
                ('dialect_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Dialect')),
            ],
        ),
        migrations.CreateModel(
            name='ResourceDialectItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('audio_url', models.FileField(blank=True, null=True, upload_to='', validators=[polls.models.validate_audio_extension])),
                ('dialect', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.Dialect')),
            ],
        ),
        migrations.CreateModel(
            name='ResourceItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=200)),
                ('word_in_language', models.CharField(blank=True, default='', max_length=200)),
                ('pronounciation_guide_or_date', models.CharField(blank=True, max_length=200)),
                ('audio_url', models.FileField(blank=True, null=True, upload_to='', validators=[polls.models.validate_audio_extension])),
                ('resource_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Resource')),
            ],
        ),
        migrations.CreateModel(
            name='ResourceItemPicture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phrase', models.CharField(max_length=200)),
                ('phrase_in_language', models.CharField(max_length=200)),
                ('picture_url', models.FileField(blank=True, null=True, upload_to='', validators=[polls.models.validate_picture_extension])),
                ('audio_url', models.FileField(blank=True, null=True, upload_to='', validators=[polls.models.validate_audio_extension])),
                ('resource_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Resource')),
            ],
        ),
        migrations.CreateModel(
            name='SituationalVideo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('situation_description', models.CharField(max_length=200)),
                ('situation_description_in_language', models.CharField(blank=True, max_length=200)),
                ('video_with_transcript', models.FileField(blank=True, null=True, upload_to='', validators=[polls.models.validate_movie_extension])),
                ('video_without_transcript', models.FileField(blank=True, null=True, upload_to='', validators=[polls.models.validate_movie_extension])),
                ('question_text', models.CharField(blank=True, max_length=200)),
                ('choice_1', models.CharField(blank=True, max_length=200)),
                ('choice_2', models.CharField(blank=True, max_length=200)),
                ('choice_3', models.CharField(blank=True, max_length=200)),
                ('choice_4', models.CharField(blank=True, max_length=200)),
                ('choice_5', models.CharField(blank=True, max_length=200)),
                ('choice_6', models.CharField(blank=True, max_length=200)),
                ('correct_answers', models.CharField(blank=True, max_length=200)),
                ('language_topic', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.LanguageTopic')),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic_name', models.CharField(max_length=200, unique=True)),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Level')),
            ],
        ),
        migrations.AddField(
            model_name='resourcedialectitem',
            name='resource_item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.ResourceItem'),
        ),
        migrations.AddField(
            model_name='languagetopic',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Topic'),
        ),
        migrations.AddField(
            model_name='languagesubtopic',
            name='language_topic',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.LanguageTopic'),
        ),
        migrations.AddField(
            model_name='glossary',
            name='language_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Language'),
        ),
        migrations.AddField(
            model_name='exercise',
            name='language_subtopic',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.LanguageSubtopic'),
        ),
        migrations.AddField(
            model_name='dialect',
            name='language_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Language'),
        ),
    ]
