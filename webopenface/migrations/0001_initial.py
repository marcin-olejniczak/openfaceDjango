# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-15 14:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DetectedFace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('face', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='DetectedPeople',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('face', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webopenface.DetectedFace')),
            ],
        ),
        migrations.CreateModel(
            name='Frame',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frame', models.TextField()),
                ('add_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='PeopleFace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('face', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('add_date', models.DateTimeField()),
                ('mod_date', models.DateTimeField()),
            ],
            options={
                'verbose_name_plural': 'people',
            },
        ),
        migrations.AddField(
            model_name='peopleface',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webopenface.Person'),
        ),
        migrations.AddField(
            model_name='detectedpeople',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webopenface.Person'),
        ),
        migrations.AddField(
            model_name='detectedface',
            name='frame',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webopenface.Frame'),
        ),
    ]
