# Generated by Django 3.0.7 on 2021-08-15 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banking', '0003_auto_20210813_2009'),
    ]

    operations = [
        migrations.CreateModel(
            name='After',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('sender', models.CharField(max_length=30)),
                ('receiver', models.CharField(max_length=30)),
                ('amt', models.IntegerField()),
            ],
        ),
    ]