# Generated by Django 2.0.3 on 2018-05-02 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cias', '0004_auto_20180425_0415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='impactevent',
            name='severity',
            field=models.FloatField(),
        ),
    ]