# Generated by Django 4.1.7 on 2023-04-08 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='uav',
            name='max_range',
            field=models.PositiveIntegerField(default=0, verbose_name='Макс. дальность туда и обратно'),
            preserve_default=False,
        ),
    ]
