# Generated by Django 2.0.6 on 2018-08-04 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coderdojomobile', '0007_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='comment',
            field=models.CharField(max_length=1500, null=True),
        ),
        migrations.AlterField(
            model_name='rating',
            name='rating_author',
            field=models.CharField(max_length=150, null=True),
        ),
    ]