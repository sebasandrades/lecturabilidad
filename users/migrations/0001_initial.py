# Generated by Django 3.0.6 on 2020-06-05 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resultado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('perspicuidad', models.FloatField(max_length=20)),
            ],
        ),
    ]