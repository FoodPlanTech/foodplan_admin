# Generated by Django 4.2.5 on 2023-09-29 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_telegramaccount_telegram_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='telegramaccount',
            name='telegram_id',
            field=models.BigIntegerField(unique=True, verbose_name='Telegram ID'),
        ),
    ]
