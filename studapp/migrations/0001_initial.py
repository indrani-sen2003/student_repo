# Generated by Django 2.2.16 on 2020-10-29 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='stud',
            fields=[
                ('roll', models.IntegerField(primary_key=True, serialize=False)),
                ('sname', models.CharField(max_length=30)),
                ('dob', models.DateField()),
            ],
        ),
    ]
