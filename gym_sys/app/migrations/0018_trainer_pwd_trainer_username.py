# Generated by Django 5.0.1 on 2024-01-24 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_trainer'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainer',
            name='pwd',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='trainer',
            name='username',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
