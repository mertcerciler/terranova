# Generated by Django 2.2.4 on 2019-10-02 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bloglar', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='resim2',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
