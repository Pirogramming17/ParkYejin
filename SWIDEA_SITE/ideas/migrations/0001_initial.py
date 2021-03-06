# Generated by Django 4.0.6 on 2022-07-20 13:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tool',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='이름')),
                ('kind', models.CharField(max_length=100, verbose_name='종류')),
                ('content', models.TextField(max_length=100, verbose_name='내용')),
            ],
        ),
        migrations.CreateModel(
            name='Idea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='제목')),
                ('image', models.ImageField(blank=True, upload_to='ideas/%Y%m%d', verbose_name='사진')),
                ('content', models.TextField(verbose_name='설명')),
                ('interest', models.CharField(max_length=100, verbose_name='관심도')),
                ('devtool', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dev_tool', to='ideas.tool', verbose_name='개발툴')),
            ],
        ),
    ]
