# Generated by Django 3.1.5 on 2021-01-08 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post1_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post1',
            name='slug',
            field=models.CharField(max_length=130),
        ),
    ]