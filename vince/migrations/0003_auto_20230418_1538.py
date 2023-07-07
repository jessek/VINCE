# Generated by Django 3.2.18 on 2023-04-18 15:38

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vince', '0002_auto_20230412_1902'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productversion',
            name='cve',
        ),
        migrations.AddField(
            model_name='productversion',
            name='cve',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='vince.cveallocation'),
        ),
        migrations.RemoveField(
            model_name='vendorproduct',
            name='sector',
        ),
        migrations.AddField(
            model_name='vendorproduct',
            name='sector',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=50), blank=True, null=True, size=None),
        ),
    ]