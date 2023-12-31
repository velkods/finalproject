# Generated by Django 4.2.3 on 2023-07-20 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=120)),
                ('title', models.CharField(max_length=120, verbose_name='Product Name')),
                ('image', models.FileField(upload_to='')),
                ('price', models.FloatField(verbose_name='Price')),
                ('description', models.TextField(blank=True)),
                ('availability', models.BooleanField()),
                ('date', models.DateTimeField(verbose_name='Release Date')),
            ],
        ),
    ]
