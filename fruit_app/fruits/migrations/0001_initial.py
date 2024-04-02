# Generated by Django 5.0.3 on 2024-04-01 13:01

import django.core.validators
import django.db.models.deletion
import fruit_app.fruits.custom_validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fruit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fruit_name', models.CharField(max_length=30, unique=True, validators=[django.core.validators.MinLengthValidator(2), fruit_app.fruits.custom_validators.validate_all_letters], verbose_name='Name')),
                ('fruit_image_url', models.URLField(verbose_name='Image URL')),
                ('description', models.TextField()),
                ('nutrition_info', models.TextField(blank=True, null=True, verbose_name='Nutrition')),
                ('owner', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='profiles.profile')),
            ],
        ),
    ]
