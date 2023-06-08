# Generated by Django 4.1.5 on 2023-06-02 11:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('caremax', '0018_bill_bill'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='patient_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='display_bills', to='caremax.patient'),
        ),
    ]
