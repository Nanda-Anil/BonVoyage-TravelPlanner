# Generated by Django 4.1.7 on 2023-02-25 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bonvoyage_app', '0003_uploadmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='bookmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agency', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=300)),
                ('spots', models.CharField(max_length=500)),
                ('rate', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=20)),
                ('frmdy', models.CharField(max_length=20)),
                ('tody', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
            ],
        ),
    ]