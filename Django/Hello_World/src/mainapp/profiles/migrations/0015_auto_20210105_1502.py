# Generated by Django 3.1.4 on 2021-01-05 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0014_auto_20210105_1414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profiles',
            name='type',
            field=models.CharField(choices=[("Ma'am", "Ma'am"), ('Mrs', 'Mrs'), ('Mr.', 'Mr.'), ('Ms', 'Ms'), ('Sir', 'Sir')], max_length=60),
        ),
    ]
