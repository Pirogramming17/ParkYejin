# Generated by Django 4.0.6 on 2022-07-20 19:32

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ideas', '0003_alter_idea_interest'),
    ]

    operations = [
        migrations.DeleteModel(
            name='IdeaStar',
        ),
        migrations.AlterField(
            model_name='idea',
            name='interest',
            field=models.IntegerField(verbose_name='관심도'),
        ),
        migrations.RemoveField(
            model_name='idea',
            name='like',
        ),
        migrations.AddField(
            model_name='idea',
            name='like',
            field=models.ManyToManyField(blank='True', related_name='IdeaLike', to=settings.AUTH_USER_MODEL, verbose_name='찜하기'),
        ),
    ]
