# Generated by Django 5.0.1 on 2024-01-31 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0031_alter_trainersalary_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='trainersalary',
            options={'verbose_name_plural': 'Trainer Salary'},
        ),
        migrations.AlterField(
            model_name='trainersalary',
            name='remarks',
            field=models.TextField(blank=True),
        ),
    ]