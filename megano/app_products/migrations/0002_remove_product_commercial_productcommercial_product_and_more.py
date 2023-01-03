# Generated by Django 4.1.2 on 2023-01-03 17:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='commercial',
        ),
        migrations.AddField(
            model_name='productcommercial',
            name='product',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='product.product', verbose_name='Product'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='productcommercial',
            name='count',
            field=models.IntegerField(verbose_name='left in stock'),
        ),
    ]