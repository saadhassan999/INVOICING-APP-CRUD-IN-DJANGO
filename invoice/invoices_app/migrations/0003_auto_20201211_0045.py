# Generated by Django 3.1.2 on 2020-12-10 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoices_app', '0002_auto_20201211_0043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoices',
            name='unit_cost',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
    ]
