# Generated by Django 4.0.6 on 2022-07-20 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ideas', '0004_delete_ideastar_alter_idea_interest_remove_idea_like_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='idea',
            name='like',
        ),
        migrations.AddField(
            model_name='idea',
            name='like',
            field=models.BooleanField(default=False, verbose_name='찜하기'),
        ),
    ]
