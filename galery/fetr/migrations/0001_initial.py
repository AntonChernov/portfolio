# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('album_picture', models.ImageField(upload_to=b'/home/tito/www/galery/fetr/static/images/')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'/home/tito/www/galery/fetr/static/images/')),
                ('image_name', models.CharField(max_length=100)),
                ('album', models.ForeignKey(to='fetr.Album')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
