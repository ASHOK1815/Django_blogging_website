# Generated by Django 3.1.5 on 2021-01-08 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post1',
            name='slug',
            field=models.CharField(default=1, max_length=13),
            preserve_default=False,
        ),
    ]
