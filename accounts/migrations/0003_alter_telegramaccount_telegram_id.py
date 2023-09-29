# Generated by Django 4.2.5 on 2023-09-29 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_telegramaccount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='telegramaccount',
            name='telegram_id',
            field=models.PositiveIntegerField(unique=True, verbose_name='Telegram ID'),
        ),
    ]