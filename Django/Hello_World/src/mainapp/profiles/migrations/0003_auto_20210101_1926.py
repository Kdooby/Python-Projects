# Generated by Django 3.1.4 on 2021-01-02 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20210101_1924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profiles',
            name='type',
            field=models.CharField(choices=[('Mr.', 'Mr.'), ('Ms', 'Ms'), ("Ma'am", "Ma'am"), ('Mrs', 'Mrs'), ('Sir', 'Sir')], max_length=60),
        ),
    ]
