# Generated by Django 5.0.2 on 2024-03-03 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_rename_proapp_product_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('motu', 'CC'), ('oagy', 'CC'), ('chotabheem', 'CC'), ('doremon', 'CC'), ('teddy', 'td'), ('combo toy', 'CT')], max_length=10),
        ),
    ]