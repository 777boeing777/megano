# Generated by Django 4.1.5 on 2023-01-15 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_rename_categories_productcommercial_highlights'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product',
            field=models.JSONField(null=True, verbose_name='the product characters'),
        ),
    ]