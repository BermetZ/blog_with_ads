# Generated by Django 2.1.7 on 2019-03-28 17:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='ad', to='ads.Ad')),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=1000)),
                ('phone', models.IntegerField()),
                ('logo', models.ImageField(blank=True, null=True, upload_to='logo')),
            ],
            options={
                'verbose_name': 'Company',
                'verbose_name_plural': 'Companies',
            },
        ),
        migrations.AddField(
            model_name='ad',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='company', to='ads.Company'),
        ),
    ]
