# Generated by Django 3.1.5 on 2021-01-19 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll_no', models.TextField()),
                ('name', models.TextField(max_length=40)),
                ('stud_class', models.TextField()),
                ('department', models.TextField()),
            ],
        ),
    ]
