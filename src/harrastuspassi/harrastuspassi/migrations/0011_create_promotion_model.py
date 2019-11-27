# Generated by Django 2.2.4 on 2019-11-08 06:33

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('harrastuspassi', '0010_category_name_not_unique'),
    ]

    operations = [
        migrations.CreateModel(
            name='Promotion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=1024)),
                ('description', models.TextField()),
                ('start_date', models.DateField(verbose_name='Start date')),
                ('start_time', models.TimeField(verbose_name='Start time')),
                ('end_date', models.DateField(verbose_name='End date')),
                ('end_time', models.TimeField(verbose_name='End time')),
                ('cover_image', models.ImageField(blank=True, null=True, upload_to='promo_images')),
                ('hobby', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='harrastuspassi.Hobby')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
