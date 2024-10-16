# Generated by Django 4.2 on 2024-10-04 08:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('conferences', '0002_alter_conference_category'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('confirmed', models.BooleanField(default=False)),
                ('reservation_date', models.DateTimeField(auto_now_add=True)),
                ('conference', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='conferences.conference')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('conference', 'participant')},
            },
        ),
        migrations.AddField(
            model_name='participant',
            name='reservations',
            field=models.ManyToManyField(related_name='reservations', through='users.reservation', to='conferences.conference'),
        ),
    ]
