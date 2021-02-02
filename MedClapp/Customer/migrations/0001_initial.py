# Generated by Django 3.1.5 on 2021-01-15 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customerprofile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.CharField(max_length=4)),
                ('bloodgroup', models.CharField(choices=[('A+', 'A+'), ('B+', 'B+'), ('AB+', 'AB+'), ('O+', 'O+'), ('A-', 'A-'), ('B-', 'B-'), ('AB-', 'AB-'), ('O-', 'O-')], max_length=100)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=100)),
                ('height', models.CharField(default=None, max_length=10)),
                ('weight', models.CharField(default=None, max_length=10)),
                ('address', models.TextField(max_length=250)),
                ('image', models.ImageField(default=None, upload_to='images')),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bloodgrouprequest', models.CharField(choices=[('A+', 'A+'), ('B+', 'B+'), ('AB+', 'AB+'), ('O+', 'O+'), ('A-', 'A-'), ('B-', 'B-'), ('AB-', 'AB-'), ('O-', 'O-')], max_length=100)),
                ('location', models.TextField(max_length=250)),
                ('priority', models.CharField(choices=[('Emergency', 'Emergency'), ('Moderate', 'Moderate'), ('Normal', 'Normal')], max_length=100)),
            ],
        ),
    ]