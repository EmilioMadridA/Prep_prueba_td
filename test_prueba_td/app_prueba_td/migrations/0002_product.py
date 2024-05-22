# Generated by Django 4.2.11 on 2024-05-22 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_prueba_td', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='products/')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('public', models.BooleanField(default=True)),
            ],
        ),
    ]