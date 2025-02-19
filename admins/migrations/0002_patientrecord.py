# Generated by Django 5.0.6 on 2024-05-27 08:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PatientRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medical_history', models.TextField()),
                ('diagnosis', models.TextField()),
                ('medications', models.TextField()),
                ('allergies', models.TextField()),
                ('treatment_history', models.TextField()),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admins.patient')),
            ],
        ),
    ]
