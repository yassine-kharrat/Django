# Generated by Django 4.2 on 2024-10-04 08:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
        ('conferences', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conference',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='conferences', to='categories.category'),
        ),
    ]
