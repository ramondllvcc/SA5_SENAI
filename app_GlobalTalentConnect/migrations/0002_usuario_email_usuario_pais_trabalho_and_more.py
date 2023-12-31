# Generated by Django 5.0 on 2023-12-18 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_GlobalTalentConnect', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='email',
            field=models.EmailField(default='example@example.com', max_length=254),
        ),
        migrations.AddField(
            model_name='usuario',
            name='pais_trabalho',
            field=models.CharField(default='Brasil', max_length=255),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='nome',
            field=models.TextField(max_length=255),
        ),
    ]
