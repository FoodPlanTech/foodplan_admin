# Generated by Django 4.2.5 on 2023-09-29 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_telegramaccount_telegram_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='telegramaccount',
            name='id',
        ),
        migrations.AlterField(
            model_name='telegramaccount',
            name='telegram_id',
            field=models.BigIntegerField(primary_key=True, serialize=False, verbose_name='Telegram ID'),
        ),
    ]
