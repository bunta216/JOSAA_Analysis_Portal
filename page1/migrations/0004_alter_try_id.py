# Generated by Django 4.2.3 on 2023-07-13 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page1', '0003_alter_try_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='try',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]