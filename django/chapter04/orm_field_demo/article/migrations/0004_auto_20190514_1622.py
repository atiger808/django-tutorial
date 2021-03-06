# Generated by Django 2.0 on 2019-05-14 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_auto_20190514_1554'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='create_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='article',
            name='title',
            field=models.CharField(default='九月的雨', max_length=200),
            preserve_default=False,
        ),
    ]
