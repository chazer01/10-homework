# Generated by Django 5.1.4 on 2024-12-13 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note_title', models.CharField(max_length=100)),
                ('content', models.CharField(max_length=100)),
            ],
        ),
    ]
