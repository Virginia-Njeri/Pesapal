# Generated by Django 4.1 on 2022-09-02 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0008_alter_customer_employment_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='employment_status',
            field=models.BooleanField(max_length=30, null=True),
        ),
    ]