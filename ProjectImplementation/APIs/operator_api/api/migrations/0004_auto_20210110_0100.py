# Generated by Django 2.2.17 on 2021-01-10 01:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20210109_1815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='catalogue',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='item', to='api.Catalogue'),
        ),
    ]
