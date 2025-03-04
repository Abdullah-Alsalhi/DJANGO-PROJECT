# Generated by Django 4.0.6 on 2022-08-04 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(null=True)),
                ('quantity', models.IntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='electronic',
            name='brand',
        ),
        migrations.AlterField(
            model_name='brand',
            name='name',
            field=models.CharField(default='', max_length=255, unique=True),
            preserve_default=False,
        ),
    ]
