# Generated by Django 3.1.7 on 2021-03-21 20:21

from django.db import migrations, models
import mainapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_auto_20210321_2149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(null=True, upload_to=mainapp.models.Post.get_file_name_posts),
        ),
    ]
