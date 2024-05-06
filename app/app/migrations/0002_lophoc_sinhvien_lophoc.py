# Generated by Django 5.0.3 on 2024-03-30 08:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lophoc',
            fields=[
                ('ma_lop', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('ten_lop', models.CharField(max_length=50, null=True)),
                ('slug_lop', models.SlugField(unique=True)),
                ('lop', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lop_hoc', to='app.lophoc')),
            ],
        ),
        migrations.AddField(
            model_name='sinhvien',
            name='lophoc',
            field=models.ManyToManyField(related_name='thuoc_lop', to='app.lophoc'),
        ),
    ]