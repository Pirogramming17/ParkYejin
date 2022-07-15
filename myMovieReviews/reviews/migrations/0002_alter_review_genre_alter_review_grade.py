# Generated by Django 4.0.6 on 2022-07-15 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='genre',
            field=models.CharField(choices=[('액션', 'Action'), ('코미디', 'Comedy'), ('범죄', 'Crime'), ('판타지', 'Fantasy'), ('공포', 'Horror'), ('로맨스', 'Romance'), ('공상과학', 'SF')], max_length=50),
        ),
        migrations.AlterField(
            model_name='review',
            name='grade',
            field=models.DecimalField(decimal_places=1, max_digits=10, verbose_name='별점'),
        ),
    ]
