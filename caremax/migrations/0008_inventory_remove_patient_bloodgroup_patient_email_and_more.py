# Generated by Django 4.1.5 on 2023-02-24 09:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('caremax', '0007_alter_test_patient_id_alter_treatment_patient_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=100)),
                ('rate', models.IntegerField()),
                ('amount_received', models.IntegerField()),
                ('amount_dispensed', models.IntegerField()),
                ('balance', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='patient',
            name='bloodgroup',
        ),
        migrations.AddField(
            model_name='patient',
            name='email',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='gender',
            field=models.CharField(max_length=7, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='relationship',
            field=models.CharField(max_length=7, null=True),
        ),
        migrations.AddField(
            model_name='test',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='treatment',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='contact',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='nextofkin',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('amountpaid', models.IntegerField()),
                ('balance', models.IntegerField()),
                ('patient_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='display_bill', to='caremax.patient')),
            ],
        ),
    ]
