# Generated by Django 4.1.3 on 2022-12-10 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GiveAway', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='ItemImage',
            field=models.ImageField(upload_to='freebies'),
        ),
    ]
