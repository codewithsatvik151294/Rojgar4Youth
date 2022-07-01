# Generated by Django 3.1.3 on 2021-09-01 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fourYouthAPI', '0009_auto_20210831_1223'),
    ]

    operations = [
        migrations.CreateModel(
            name='OtpDbModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobNO', models.CharField(blank=True, max_length=11)),
                ('otpCode', models.CharField(blank=True, max_length=6)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddConstraint(
            model_name='otpdbmodel',
            constraint=models.UniqueConstraint(fields=('mobNO', 'otpCode'), name='OtpDbModel Constraints'),
        ),
    ]
