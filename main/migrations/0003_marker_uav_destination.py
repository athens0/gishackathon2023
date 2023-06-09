# Generated by Django 4.1.7 on 2023-04-09 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_uav_max_range'),
    ]

    operations = [
        migrations.CreateModel(
            name='Marker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('uav_id', models.PositiveIntegerField(verbose_name='БПЛА')),
                ('description', models.TextField(verbose_name='Описание')),
                ('state', models.PositiveIntegerField(verbose_name='Состояние')),
                ('marker', models.PositiveIntegerField(verbose_name='Маркер')),
                ('cord_x', models.CharField(max_length=100, verbose_name='Расположение по широте')),
                ('cord_y', models.CharField(max_length=100, verbose_name='Расположение по высоте')),
            ],
            options={
                'verbose_name': 'Маркер',
                'verbose_name_plural': 'Маркеры',
            },
        ),
        migrations.AddField(
            model_name='uav',
            name='destination',
            field=models.PositiveBigIntegerField(default=1, verbose_name='Направление'),
            preserve_default=False,
        ),
    ]
