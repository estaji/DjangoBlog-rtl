# Generated by Django 3.2 on 2021-04-28 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogcore', '0002_auto_20210428_2009'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ManyToManyField(to='blogcore.Category', verbose_name='دسته بندی'),
        ),
    ]
