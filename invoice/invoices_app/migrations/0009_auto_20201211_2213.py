# Generated by Django 3.1.2 on 2020-12-11 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoices_app', '0008_auto_20201211_2212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='invoice_id',
            field=models.AutoField(default='1', primary_key=True, serialize=False),
        ),
    ]
