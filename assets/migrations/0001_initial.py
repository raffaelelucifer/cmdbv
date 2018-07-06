# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('slug', models.CharField(max_length=100)),
                ('desc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('slug', models.CharField(max_length=100, null=True, blank=True)),
                ('pm', models.CharField(max_length=30)),
                ('telephone', models.CharField(max_length=11)),
                ('git_url', models.URLField()),
                ('desc', models.TextField()),
                ('product_name', models.ForeignKey(to='assets.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('ipaddress', models.CharField(max_length=30)),
                ('mac', models.CharField(max_length=30, null=True, blank=True)),
                ('CPU', models.CharField(max_length=30)),
                ('memcache', models.CharField(max_length=10)),
                ('space', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Server_Brand',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('ipaddress', models.CharField(max_length=50)),
                ('status', models.BooleanField()),
                ('server_name', models.ForeignKey(to='assets.Server')),
            ],
        ),
        migrations.AddField(
            model_name='server',
            name='brand',
            field=models.ForeignKey(to='assets.Server_Brand'),
        ),
        migrations.AddField(
            model_name='server',
            name='project_name',
            field=models.ManyToManyField(to='assets.Project'),
        ),
    ]
