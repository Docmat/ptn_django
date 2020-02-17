# Generated by Django 2.2 on 2020-02-14 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('posts', '0002_auto_20200214_1407'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('post', models.ManyToManyField(related_name='tags', to='posts.Post')),
            ],
        ),
    ]
