# Generated by Django 2.0.6 on 2018-08-10 10:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Computer',
            fields=[
                ('hostname', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('foreign_timestamp', models.IntegerField(default=0)),
                ('local_timestamp', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('username', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('last_ping', models.IntegerField(default=0)),
                ('time_spent', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='computer',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='tracker.User'),
        ),
    ]