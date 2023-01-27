# Generated by Django 4.1.5 on 2023-01-27 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_image', models.ImageField(upload_to='post_images/')),
                ('post_text', models.CharField(max_length=300)),
                ('post_title', models.CharField(max_length=30)),
                ('post_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
