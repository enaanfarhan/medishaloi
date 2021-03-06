# Generated by Django 2.2.4 on 2019-08-19 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ambulance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200)),
                ('image', models.FileField(blank=True, upload_to='')),
                ('address', models.CharField(blank=True, max_length=200)),
                ('hospital_name', models.CharField(blank=True, max_length=200)),
                ('mobile', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(blank=True, upload_to='')),
                ('doctor_name', models.CharField(blank=True, max_length=200)),
                ('specialist', models.CharField(blank=True, max_length=200)),
                ('lacation', models.CharField(blank=True, max_length=100)),
                ('education_background', models.CharField(blank=True, max_length=300)),
                ('phone', models.CharField(blank=True, max_length=50)),
                ('address', models.CharField(blank=True, max_length=300)),
                ('user_reviwe', models.CharField(blank=True, max_length=60)),
                ('description', models.CharField(blank=True, max_length=600)),
            ],
        ),
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200)),
                ('image', models.FileField(blank=True, upload_to='')),
                ('company_name', models.CharField(blank=True, max_length=200)),
                ('group_name', models.CharField(blank=True, max_length=200)),
                ('indication', models.CharField(blank=True, max_length=600)),
                ('dose', models.CharField(blank=True, max_length=600)),
                ('side_effect', models.CharField(blank=True, max_length=600)),
                ('type', models.CharField(blank=True, max_length=200)),
                ('price', models.CharField(blank=True, max_length=200)),
            ],
        ),
    ]
