# Generated by Django 4.2.1 on 2023-06-04 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='asset',
            name='name',
        ),
        migrations.AddField(
            model_name='asset',
            name='checkedOutCondition',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='asset',
            name='device_type',
            field=models.CharField(blank=True, choices=[('phone', 'Phone'), ('tablet', 'Tablet'), ('laptop', 'Laptop'), ('other', 'Other')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='asset',
            name='newCondition',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='asset',
            name='checked_out_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='asset',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='asset',
            name='returned_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]