# Generated by Django 3.0.2 on 2020-02-03 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='My_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25)),
                ('pdf', models.FileField(upload_to='static/media')),
            ],
        ),
        migrations.CreateModel(
            name='signup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=40)),
                ('Email', models.CharField(max_length=40)),
                ('Phone', models.CharField(max_length=40)),
                ('Password', models.CharField(max_length=40)),
            ],
        ),
    ]
