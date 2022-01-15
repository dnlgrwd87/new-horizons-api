# Generated by Django 4.0.1 on 2022-01-15 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Villager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('icon_image', models.CharField(max_length=256)),
                ('house_image', models.CharField(max_length=256)),
                ('species', models.CharField(max_length=256)),
                ('gender', models.CharField(max_length=256)),
                ('personality', models.CharField(max_length=256)),
                ('birthday', models.CharField(max_length=256)),
                ('catchphrase', models.CharField(max_length=256)),
                ('style1', models.CharField(max_length=256)),
                ('style2', models.CharField(max_length=256)),
                ('color1', models.CharField(max_length=256)),
                ('color2', models.CharField(max_length=256)),
                ('spreadsheet_id', models.CharField(max_length=256)),
            ],
        ),
    ]
