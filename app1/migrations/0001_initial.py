# Generated by Django 5.0.3 on 2024-04-06 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('property_type', models.CharField(choices=[('residential', 'Residential'), ('commercial', 'Commercial'), ('land', 'Land'), ('industrial', 'Industrial'), ('special_purpose', 'Special Purpose')], max_length=20)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('bedrooms', models.PositiveIntegerField()),
                ('bathrooms', models.PositiveIntegerField()),
                ('size_sqft', models.PositiveIntegerField()),
                ('lot_size_acres', models.DecimalField(decimal_places=2, max_digits=10)),
                ('year_built', models.PositiveIntegerField()),
                ('location', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('listed_date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
