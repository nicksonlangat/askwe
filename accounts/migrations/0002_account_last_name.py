# Generated by Django 3.0.5 on 2020-04-12 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='last_name',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
    ]
