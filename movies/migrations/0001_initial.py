# Generated by Django 3.0.5 on 2020-04-27 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, null=True, verbose_name='Movie Title')),
                ('synopsys', models.CharField(blank=True, max_length=100, null=True, verbose_name='Synospys')),
                ('release_year', models.CharField(blank=True, max_length=100, null=True, verbose_name='Release year')),
                ('duration', models.IntegerField(blank=True, default=10, null=True, verbose_name='Duration')),
            ],
        ),
    ]
