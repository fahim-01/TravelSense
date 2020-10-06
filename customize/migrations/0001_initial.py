# Generated by Django 3.1.1 on 2020-09-27 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Destination_name', models.CharField(max_length=100)),
                ('category', models.CharField(default='', max_length=50)),
                ('subcategory', models.CharField(default='', max_length=50)),
                ('image', models.ImageField(default='0', upload_to='shop/images')),
                ('desc', models.CharField(max_length=600)),
                ('price', models.IntegerField(default=0)),
            ],
        ),
    ]
