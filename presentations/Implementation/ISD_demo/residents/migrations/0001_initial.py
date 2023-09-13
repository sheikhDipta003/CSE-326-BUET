# Generated by Django 4.2.4 on 2023-09-03 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CheckupItem',
            fields=[
                ('Checkup_Id', models.AutoField(primary_key=True, serialize=False)),
                ('Blood_Pressure', models.CharField(max_length=20)),
                ('Sugar', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Heartrate', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='MedCond',
            fields=[
                ('Cond_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=50)),
                ('Advice', models.CharField(max_length=150)),
                ('Guideline', models.CharField(max_length=150)),
            ],
        ),
    ]
