# Generated by Django 4.1.7 on 2023-02-25 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bonvoyage_app', '0002_agencyregmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='uploadmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agency', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('state', models.CharField(max_length=30)),
                ('spots', models.CharField(max_length=500)),
                ('food', models.CharField(choices=[('food', 'food'), ('yes', 'yes'), ('no', 'no')], max_length=30)),
                ('pet', models.CharField(choices=[('pet', 'pet'), ('yes', 'yes'), ('no', 'no')], max_length=30)),
                ('duration', models.CharField(choices=[('0-0', '0-0'), ('0-1', '0-1'), ('1-2', '1-2'), ('2-3', '2-3'), ('3-4', '3-4'), ('4-5', '4-5'), ('5-6', '5-6'), ('6-7', '6-7'), ('7-8', '7-8'), ('8-9', '8-9'), ('9-10', '9-10')], max_length=30)),
                ('cab', models.CharField(choices=[('cab', 'cab'), ('yes', 'yes'), ('no', 'no')], max_length=30)),
                ('stay', models.CharField(max_length=30)),
                ('rate', models.CharField(max_length=30)),
            ],
        ),
    ]