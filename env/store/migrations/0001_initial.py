# Generated by Django 4.0.3 on 2022-04-04 14:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=255)),
                ('Slug', models.SlugField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=255)),
                ('Manufacturer', models.CharField(default='admin', max_length=255)),
                ('Description', models.TextField(blank=True)),
                ('image', models.ImageField(upload_to='images/')),
                ('Slug', models.SlugField(max_length=255, unique='True')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('in_stock', models.BooleanField(default='True')),
                ('is_active', models.BooleanField(default='True')),
                ('Created', models.DateTimeField(auto_now_add=True)),
                ('Upadted', models.DateTimeField(auto_now_add=True)),
                ('Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Product', to='store.category')),
                ('Created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Product_creator', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
