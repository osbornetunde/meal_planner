# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-11 22:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meal_plan', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nutrient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('meal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meal_plan.Meal')),
            ],
            options={
                'verbose_name_plural': 'entries',
            },
        ),
    ]
