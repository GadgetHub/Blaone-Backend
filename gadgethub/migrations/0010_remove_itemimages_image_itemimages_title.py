# Generated by Django 4.1.3 on 2023-03-21 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gadgethub', '0009_itemimages'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itemimages',
            name='image',
        ),
        migrations.AddField(
            model_name='itemimages',
            name='title',
            field=models.CharField(blank=True, max_length=200000, null=True),
        ),
    ]