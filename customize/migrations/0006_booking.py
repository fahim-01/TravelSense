# Generated by Django 3.1.1 on 2020-09-29 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customize', '0005_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('booking_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(default='', max_length=100)),
                ('departure', models.CharField(default='', max_length=100)),
                ('destination', models.CharField(default='', max_length=100)),
                ('number_Of_Guests', models.IntegerField(default='', verbose_name=100)),
                ('phone', models.CharField(default='', max_length=100)),
                ('desc', models.CharField(default='', max_length=10000)),
            ],
        ),
    ]
