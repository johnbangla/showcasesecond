# Generated by Django 3.0.7 on 2020-07-12 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_extraimage_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carosalimages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=10, null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
