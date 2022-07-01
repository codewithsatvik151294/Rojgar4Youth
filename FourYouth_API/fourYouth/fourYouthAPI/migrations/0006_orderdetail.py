# Generated by Django 3.1.3 on 2021-08-10 06:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fourYouthAPI', '0005_auto_20210805_1614'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderID', models.CharField(blank=True, max_length=20)),
                ('pay_status', models.CharField(blank=True, max_length=20)),
                ('pay_type', models.CharField(blank=True, max_length=20)),
                ('remarks', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('addressfk', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='fourYouthAPI.addresslistedbyuser')),
                ('productInfoM2M', models.ManyToManyField(to='fourYouthAPI.ProductsListing')),
                ('userfk', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
