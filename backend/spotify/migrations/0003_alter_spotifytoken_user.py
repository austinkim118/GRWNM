# Generated by Django 4.2.7 on 2023-12-04 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spotify', '0002_alter_spotifytoken_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spotifytoken',
            name='user',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
