# Generated by Django 4.1.3 on 2023-03-29 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gadgethub', '0030_orderitem_createdat_orderitem_orderitemnumber'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='isSold',
            field=models.BooleanField(default=False),
        ),
    ]
