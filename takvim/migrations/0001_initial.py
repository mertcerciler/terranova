# Generated by Django 2.2.4 on 2019-10-02 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='takvim_icerik',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('baslangic_zamani', models.CharField(max_length=5)),
                ('bitis_zamani', models.CharField(max_length=5)),
                ('icerik', models.CharField(max_length=100)),
                ('tarih', models.DateTimeField()),
            ],
        ),
    ]
