# Generated by Django 4.0.5 on 2022-07-02 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=32)),
                ('weather', models.IntegerField()),
            ],
            options={
                'verbose_name': '天気情報',
                'verbose_name_plural': '天気情報',
            },
        ),
    ]
