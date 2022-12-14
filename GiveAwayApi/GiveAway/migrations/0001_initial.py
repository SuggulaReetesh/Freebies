# Generated by Django 4.1.3 on 2022-12-04 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('ItemId', models.AutoField(primary_key=True, serialize=False)),
                ('ItemName', models.CharField(max_length=100)),
                ('ItemImage', models.CharField(max_length=500)),
                ('ItemCity', models.CharField(max_length=100)),
                ('ItemState', models.CharField(max_length=100)),
                ('ItemLandmark', models.CharField(max_length=100)),
                ('ItemCountry', models.CharField(max_length=100)),
                ('ItemPincode', models.CharField(max_length=100)),
                ('ItemDescription', models.CharField(max_length=500)),
                ('ItemRequested', models.BooleanField()),
                ('UserId', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('UserId', models.AutoField(primary_key=True, serialize=False)),
                ('UserName', models.CharField(max_length=50)),
                ('UserEmail', models.CharField(max_length=100)),
                ('UserPhoneNo', models.CharField(max_length=16)),
                ('UserAddress', models.CharField(max_length=200)),
            ],
        ),
    ]
