# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentTBL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('RegistrationNumber', models.PositiveIntegerField(unique=0)),
                ('Name', models.CharField(max_length=50)),
                ('FatherName', models.CharField(max_length=50)),
                ('slug', models.SlugField(unique=True)),
                ('DateOfBirth', models.DateField()),
                ('Contact', models.PositiveIntegerField()),
                ('Address', models.CharField(max_length=100)),
            ],
        ),
    ]
