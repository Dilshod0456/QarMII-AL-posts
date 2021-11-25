# Generated by Django 3.1 on 2021-10-06 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_post_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Line',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('discription', models.TextField()),
                ('slug', models.SlugField(max_length=20)),
            ],
        ),
    ]