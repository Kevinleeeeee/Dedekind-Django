# Generated by Django 2.0.1 on 2018-02-02 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sua', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='grade',
            field=models.IntegerField(choices=[(2016, 2016), (2017, 2017)], default=2018, verbose_name='Student Grade'),
        ),
    ]
