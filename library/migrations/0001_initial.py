# Generated by Django 5.1.4 on 2024-12-18 07:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('year_of_publication', models.IntegerField()),
                ('genre', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('publisher', models.CharField(max_length=100)),
                ('cover_image', models.ImageField(upload_to='covers/')),
                ('text_file', models.FileField(upload_to='books/')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.author')),
            ],
            options={
                'unique_together': {('title', 'author', 'year_of_publication', 'publisher')},
            },
        ),
    ]
