# Generated by Django 2.0.7 on 2018-07-22 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pyemp', '0002_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.CharField(default='yan', max_length=32),
            preserve_default=False,
        ),
    ]