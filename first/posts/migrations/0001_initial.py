# Generated by Django 2.2 on 2020-02-12 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=55)),
                ('content', models.TextField()),
                ('image', models.ImageField(upload_to='media/posts')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
