# Generated by Django 3.1.3 on 2020-11-07 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_auto_20200924_0901'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_title', models.CharField(max_length=200)),
                ('image_description', models.TextField()),
                ('image_link', models.URLField()),
                ('image_url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('email', models.EmailField(blank=True, max_length=255, null=True)),
                ('facebook', models.URLField()),
                ('instargam', models.URLField()),
                ('linkedin', models.URLField()),
                ('px500', models.URLField()),
            ],
        ),
    ]