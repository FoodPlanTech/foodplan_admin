# Generated by Django 4.2.5 on 2023-10-01 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0010_foodplan_recipes_count_foodplan_start_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodplan',
            name='start_date',
            field=models.DateField(auto_now=True, null=True, verbose_name='Начало'),
        ),
    ]
