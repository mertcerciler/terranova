# Generated by Django 2.2.4 on 2019-10-02 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hizmet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('baslik', models.CharField(max_length=64)),
                ('icerik1', models.TextField(blank=True)),
                ('icerik2', models.TextField(blank=True)),
                ('resim', models.ImageField(upload_to='')),
                ('resim2', models.ImageField(upload_to='')),
            ],
        ),
    ]
