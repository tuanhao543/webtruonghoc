# Generated by Django 5.0.3 on 2024-04-01 14:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_remove_monhoc_giang_vien'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bangdiem',
            old_name='diem_cuoi_ki',
            new_name='diem_cuoi_ky',
        ),
        migrations.RenameField(
            model_name='bangdiem',
            old_name='diem_giua_ki',
            new_name='diem_giua_ky',
        ),
    ]