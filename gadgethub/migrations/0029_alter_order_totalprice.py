# Generated by Django 4.1.3 on 2023-03-27 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gadgethub', '0028_orderitem_ispaid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='totalPrice',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
    ]