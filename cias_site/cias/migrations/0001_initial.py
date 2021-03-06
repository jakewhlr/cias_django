# Generated by Django 2.0 on 2017-12-11 07:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coach',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deviceID', models.IntegerField()),
                ('name', models.CharField(max_length=30)),
                ('phoneNumber', models.CharField(max_length=10)),
                ('emailAddress', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='ImpactEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('severity', models.IntegerField()),
                ('timestamp', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='MedicalStaff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deviceID', models.IntegerField()),
                ('name', models.CharField(max_length=30)),
                ('phoneNumber', models.CharField(max_length=10)),
                ('emailAddress', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('hardwareID', models.IntegerField()),
                ('emergencyContact', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='medicalstaff',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cias.Team'),
        ),
        migrations.AddField(
            model_name='impactevent',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cias.Player'),
        ),
        migrations.AddField(
            model_name='coach',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cias.Team'),
        ),
    ]
