# Generated by Django 4.0.6 on 2022-08-04 12:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_product_remove_electronic_brand_alter_brand_name'),
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.product'),
        ),
    ]
