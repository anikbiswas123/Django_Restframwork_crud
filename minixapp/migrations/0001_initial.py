# Generated by Django 4.2.1 on 2023-05-12 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_name', models.CharField(max_length=100)),
                ('emp_address', models.CharField(max_length=100)),
                ('emp_post', models.CharField(max_length=100)),
            ],
        ),
    ]
