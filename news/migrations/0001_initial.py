# Generated by Django 5.0.6 on 2024-07-07 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(blank=True, default=None, null=True, upload_to='media', verbose_name='Картинка')),
                ('title', models.CharField(max_length=150, verbose_name='Заголовок')),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('content', models.TextField(verbose_name='Текст поста')),
                ('time_created', models.DateTimeField(auto_now_add=True, verbose_name='Время создания поста')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='Время изменения поста')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
                'ordering': ['-time_created'],
                'indexes': [models.Index(fields=['-time_created'], name='news_news_time_cr_db8b54_idx')],
            },
        ),
    ]
