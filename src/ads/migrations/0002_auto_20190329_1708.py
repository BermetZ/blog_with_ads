# Generated by Django 2.1.7 on 2019-03-29 11:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, related_name='ad', to='ads.Ad'),
        ),
    ]