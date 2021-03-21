# Generated by Django 3.1.7 on 2021-03-21 20:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_auto_20210321_2221'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='post',
            new_name='post_being_commented',
        ),
        migrations.AddField(
            model_name='post',
            name='comment_to_post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.comment'),
        ),
    ]