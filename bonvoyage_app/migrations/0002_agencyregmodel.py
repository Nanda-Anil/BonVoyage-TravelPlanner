# Generated by Django 4.1.7 on 2023-02-25 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bonvoyage_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='agencyregmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agency', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]
