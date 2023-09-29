# Generated by Django 4.2.5 on 2023-09-29 12:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_telegramaccount_telegram_id'),
        ('subscriptions', '0003_alter_payment_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='accounts.telegramaccount'),
        ),
    ]