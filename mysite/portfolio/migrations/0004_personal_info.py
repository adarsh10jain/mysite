# Generated by Django 3.0.4 on 2021-01-25 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_auto_20210124_2307'),
    ]

    operations = [
        migrations.CreateModel(
            name='Personal_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resume', models.FileField(upload_to='')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
    ]
