# Generated by Django 3.0.2 on 2020-12-23 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('translater', '0002_auto_20201222_2352'),
    ]

    operations = [
        migrations.CreateModel(
            name='WordFromUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_word', models.CharField(max_length=50, verbose_name='Слово')),
            ],
        ),
    ]
