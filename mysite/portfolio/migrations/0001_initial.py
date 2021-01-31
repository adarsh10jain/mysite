# Generated by Django 3.0.4 on 2021-01-24 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('phone', models.CharField(max_length=10)),
                ('subject', models.CharField(max_length=50)),
                ('desc', models.TextField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('desc', models.TextField()),
                ('image', models.ImageField(upload_to='')),
                ('exe', models.FileField(blank=True, upload_to='')),
                ('date', models.DateField()),
                ('tech_used', models.TextField()),
                ('thumbnail_img', models.ImageField(upload_to='')),
            ],
        ),
    ]